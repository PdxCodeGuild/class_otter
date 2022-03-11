
# Resources:
    # The basics:
        # https://click.palletsprojects.com/en/8.0.x/
    # Packages can be used:
        # https://click.palletsprojects.com/en/8.0.x/setuptools/
        # pipenv install --editable .
            # It seems we need to reinstall when editing function names.
    # https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used
        # https://pipenv-fork.readthedocs.io/en/latest/basics.html#specifying-versions-of-a-package

from setuptools import setup

setup(
    name='hello-click',
    version='0.1.0',
    py_modules=[
        'hello',
        ],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'hello = hello:cli',
        ],
    },
)
