# Hypothesis load testing

This repository contains scripts for performing load tests against the
Hypothesis web service, in particular [h](https://github.com/hypothesis/h),
using [Locust](https://locust.io).

## Running tests manually

First, ensure that the file descriptor limit in your current shell is [sufficiently
high](https://github.com/locustio/locust/issues/496). Otherwise tests may fail with DNS resolution
errors before hitting the actual capacity limit of your h instance. On macOS and Linux, you can
check limits with `ulimit -a` and adjust them with `ulimit -n`. You should choose a limit that is
higher than the number of simulated users in your test runs.

Now install Locust and run the tests:

```sh
pip install locustio

export H_API_KEY=<your developer token>

# Disable SSL verification if your h instance doesn't have a valid SSL cert
# export VERIFY_SSL=no

locust --host=<h instance URL>
```

Navigate to http://localhost:8089 in a browser to start running tests and
view results.

See the [Locust documentation](https://docs.locust.io/en/stable/) for more
details.
