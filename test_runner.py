import inspect

import fizzbuzz_tests


def main():
    tests = [fn for (name, fn) in inspect.getmembers(fizzbuzz_tests) if
             name.startswith('test') and inspect.isfunction(fn)]
    for test in tests:
        test()


if __name__ == '__main__':
    main()
