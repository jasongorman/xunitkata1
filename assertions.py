import inspect


def assert_equals(expected_value, actual_value):
    test_name = inspect.stack()[1].function
    if actual_value == expected_value:
        print(test_name + ": PASS")
    else:
        print(test_name + ": FAIL")
        print("\tExpected {expected}, but got {actual}".format(
                expected=repr(expected_value),
                actual=repr(actual_value)))