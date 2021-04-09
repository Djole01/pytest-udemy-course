# pytest-udemy-course

Automated testing with python
Tutorial: https://www.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/


# pytest arguments 

- -m customMark : test marked tests
- -v : more detailed test overview 
- -rs : show skips
- -rx : show xfails
- (xdist) -n4 : 4 threads 
- nauto : selects nr of threads automatically


# pytest markers:
- @mark.xfail(reason="reason for fail") - fail a test / expected failure
- @mark.skip (reason="reason for skip")

- @mark.parametrize('tv_brand', [           - parametrize, example with tv brands
    ('Samsung'),
    ('Sony'),
    ('Vizio')
    ]

- @mark.customMark

pytest -m customMark    - test select custom mark


# pytest.ini - define files, classes and functions to be tested. Set custom markers.
[pytest]
python_files = test_*
python_classes = *Tests
python_functions = test_*
testpaths = tests

markers =
    smoke: All critical smoke tests
    body: All car body tests
    entertainment: All tests covering the entertainment system
    
    
# conftest.py 

Fixtures (functions) that are available to all tests in conftest directory or below.


# pytest directories workaround

To run pytest from programs root directory (no include problems),
and to still use pytest.ini and conftest.py from test directory, execute pytest like this:

From root directory: python -m pytest tests

