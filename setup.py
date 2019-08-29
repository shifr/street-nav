import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("custom=", "c", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            '--maxfail=2',
            '--cov=navigator',
            '--cov-report=xml',
            '--cov-fail-under=50',
        ]
        self.custom = None

    def finalize_options(self):
        TestCommand.finalize_options(self)

        if self.custom is not None:
            self.pytest_args.extend(self.custom.split(" "))

        self.test_args = self.pytest_args
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read_requirements(filename):
    """Read pip-formatted requirements from a file."""
    with open(filename, 'r') as f:
        return [
            line.strip() for line in f.readlines() if not (
                line.startswith('#') or line.startswith('--'))
        ]


setup(
    name='navigator',
    version='0.0.1',
    author='Vladyslav Yarema',
    description='City navigation service',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    tests_require=read_requirements('requirements-test.txt'),
    zip_safe=False,
    cmdclass={"test": PyTest},
    entry_points={
        'console_scripts': ['navigate=navigator.run:main'],
    },
)
