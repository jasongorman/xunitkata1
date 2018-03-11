import importlib.util
import inspect

import os


def run_tests(module):
    tests = [fn for (name, fn) in inspect.getmembers(module) if
             name.startswith('test') and inspect.isfunction(fn)]
    for test in tests:
        test()


if __name__ == '__main__':
    test_files = [path for path in os.listdir(os.getcwd()) if path.endswith('_tests.py')]

    for test_file in test_files:
        module_name = os.path.splitext(test_file)[0]
        spec = importlib.util.spec_from_file_location(module_name, os.path.abspath(test_file))
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)

        print("Running tests from {}".format(test_file))
        run_tests(test_module)
        print()