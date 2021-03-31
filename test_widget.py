def test_widget_functions_as_expected():  # fake test case
    assert True  # will always pass


def test_widget_fails():
    assert False  # will always fail


def some_convenience_function():  # won't get tested
    print("test123")


# pytest recognizes test_ functions as tests modules
