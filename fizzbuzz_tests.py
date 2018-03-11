from fizzbuzz import fizzbuzz
from assertions import assert_equals


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


def test_fizzbuzz_10_is_Buzz():
    assert_equals('Buzz', fizzbuzz(10))


def test_fizzbuzz_15_is_FizzBuzz():
    assert_equals('FizzBuzz', fizzbuzz(15))