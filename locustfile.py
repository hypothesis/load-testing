import os

from locust import HttpLocust, TaskSet, task


def required_env(key):
    val = os.getenv(key)
    if val is None:
        raise Exception('Required env var {} not set'.format(key))
    return val


API_KEY = required_env('H_API_KEY')
VERIFY_SSL = os.getenv('VERIFY_SSL') != 'no'


class ApiTasks(TaskSet):
    @task(weight=5)
    def search(self):
        return self._api_request('GET', '/api/search')

    @task(weight=1)
    def create_annotation(self):
        ann = {'uri': 'https://load.test/',
               'text': 'Some content',
               }
        return self._api_request('POST', '/api/annotations', ann)

    def _api_request(self, method, url, body=None):
        return self.client.request(method, url, json=body,
                                   headers=self._auth_header(),
                                   verify=VERIFY_SSL)

    def _auth_header(self):
        return {'Authorization': 'Bearer {}'.format(API_KEY)}


class ApiUser(HttpLocust):
    task_set = ApiTasks
    min_wait = 5000
    max_wait = 15000
