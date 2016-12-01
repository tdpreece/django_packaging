# An example of a reusable Django package
I've seen a number of ways of structuring Django packages and wanted
to work which I thought suited me best.

## How to use this package
Run all tests,
```
detox
```

Run all tests for specific environment, e.g.
```
tox -e py27-django18
```

To run a subset of the the tests in a specifc environment, e.g.
```
tox -e py27-django18 tests.test_models
```

## Requirements
The following is a list of what I wanted from a packaging solution.

* [x] Not include tests in package that gets installed by users
* [x] Use tox to test to make testing against many environments easier and
to test the package created by setup.py
* [x] Run tests that hit the database
* [ ] Test views
* [x] Test management commands
* [x] Run tests for one environment at a time (e.g. Python 2.7 with Django 1.8)
* [x] be able to run one test at a time
* [ ] Create a virtualenv with tox, detox and setuptools so that the versions
don't have to match the system ones
* [x] Run tests for legacy versions of Django
* [ ]coverage
* [ ] dev environment for running tests quickly during development
* [ ] a virtual environment that wraps tox so I don't have to rely on system
version for tox, detox and setuptools.

The first two points suggest that keeping the tests in
the usual location for and app `app/test` would be mean
running discovery in `src/my_package/test` but testing
the installed code (installed into tox's virtualenv).
This isn't very intuitive for anyone else using the code.

## Gotchas
* Took me a couple of runs to realise that I had django>=1.8,<1.10 in setup.py
but was trying to test a tox env of django 1.4.  After creating the environment
tox will install packages required by setup.py so was upgrading to a later
version of Django.
