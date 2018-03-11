import inspect

import sys


def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)


def test_fizzbuzz_1_is_1():
    assert_equals('1', fizzbuzz(1))


def test_fizzbuzz_2_is_2():
    assert_equals('2', fizzbuzz(2))


def test_fizzbuzz_3_is_Fizz():
    assert_equals('Fizz', fizzbuzz(3))


def test_fizzbuzz_6_is_Fizz():
    assert_equals('Fizz', fizzbuzz(6))


def test_fizzbuzz_5_is_Buzz():
    assert_equals('Buzz', fizzbuzz(5))


def main():
    tests = [fn for (name, fn) in inspect.getmembers(sys.modules[__name__])
             if name.startswith('test') and inspect.isfunction(fn)]
    for test in tests:
        test()


def assert_equals(expected_value, actual_value):
    test_name = inspect.stack()[1].function
    if actual_value == expected_value:
        print(test_name + ": PASS")
    else:
        print(test_name + ": FAIL")
        print("\tExpected {expected}, but got {actual}".format(
                expected=repr(expected_value),
                actual=repr(actual_value)))


if __name__ == '__main__':
    main()
