# An example of a reusable Django package
I've seen a number of ways of structuring Django packages and wanted
to work out which I thought suited me best.

## How to use this package
Run all tests for all environments,
```
detox
```

Run all tests for specific environment, e.g.
```
tox -e py27-django18
```

To run a subset of the tests in a specific environment, e.g.
```
tox -e py27-django18 tests.test_models
```

## Requirements
The following is a list of what I wanted from a packaging solution.

* [x] Not include tests in package that gets installed by users
* [x] Test against multiple versions of Django - tox
* [x] Test packaging (setup.py, MANIFEST ..) - tox
* [x] Run tests that hit the database
* [x] Test management commands
* [x] Run tests for one environment at a time (e.g. Python 2.7 with Django 1.8)
* [x] Be able to run one test at a time
don't Have to match the system ones
* [x] Run tests for legacy versions of Django
* [x] Coverage
* [ ] Dev environment for running tests quickly during development
* [ ] A virtual environment that wraps tox so I don't have to rely on system
version for tox, detox and setuptools.

## Solution Summary
* Use tox to manage creating virtualenvs that contain all possible
combinations of dependencies.  tox also tests that my setup.py script
is working as it should.
* Use detox to run tests for all envs in parallel.
* Putting package in src means that it can't be found by the tests run by tox
so I know I'm testing the installed package.  Also, it makes using find_packages
easier to use because I don't need to manually exclude tests.
* Run coverage with
[parallel](https://coverage.readthedocs.io/en/coverage-4.2/config.html#config-run)
enabled and specify
[paths](https://coverage.readthedocs.io/en/coverage-4.2/config.html#paths)
that can be considered
so that coverage for runs for different environments can be combined.  Thus,
I can have a statements like `if six.PY3:`  in my code and still achieve 100%
coverage.  See .coveragerc file.

## Gotchas
* Took me a couple of runs to realise that I had django>=1.8,<1.10 in setup.py
but was trying to test a tox env of django 1.4.  After creating the environment
tox will install packages required by setup.py so was upgrading to a later
version of Django.
