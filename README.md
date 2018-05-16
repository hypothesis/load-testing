# Hypothesis load testing

This repository contains scripts for performing load tests against the
Hypothesis web service, in particular [h](https://github.com/hypothesis/h),
using [Locust](https://locust.io).

## Running tests manually

```sh
pip install locustio

export H_API_KEY=<your developer token>

# Disable SSL verification if your h instance doesn't have a valid SSL cert
# export VERIFY_SSL=no

locust --host=<h instance URL>
```

Then navigate to http://localhost:8089 in a browser to start running tests.

See the [Locust documentation](https://docs.locust.io/en/stable/) for more
details.
