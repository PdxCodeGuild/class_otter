# ********************************************** #
#             Click with setuptools              #
#   click pipenv setuptools package module cli   #
#                  Version: 1.0                  #
#              Author: Bruce Stull               #
#                   2022-01-28                   #
# ********************************************** #

# Resources:
    # The basics:
        # https://click.palletsprojects.com/en/8.0.x/
    # Packages can be used:
        # https://click.palletsprojects.com/en/8.0.x/setuptools/
        # pip install --editable .
            # It seems we need to reinstall when editing function names.
    # https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used
        # https://pipenv-fork.readthedocs.io/en/latest/basics.html#specifying-versions-of-a-package

from setuptools import setup

setup(
    name='ButterscotchPi',
    version='0.1.0',
    py_modules=[
        'basic_math',
        'strings',
        ],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'hello = strings:greeting',
            'multiply = basic_math:multiply',
            'divide = basic_math:divide',
        ],
    },
)
