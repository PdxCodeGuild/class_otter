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
        # pipenv install --editable .
            # It seems we need to reinstall when editing function names.
    # https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used
        # https://pipenv-fork.readthedocs.io/en/latest/basics.html#specifying-versions-of-a-package

from setuptools import setup

setup(
    name='butterscotch_pi',
    version='0.1.0',
    py_modules=[
        'strings',
        'basic_math',
        'trig_math',
        'linear_equations',
        ],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'hello = strings:greeting',
            'add = basic_math:add',
            'subtract = basic_math:subtract',
            'multiply = basic_math:multiply',
            'divide = basic_math:divide',
            'linear_ps = linear_equations:linear_ps',
            'basic_math = basic_math:the_maths',
            'trig_math = trig_math:the_trig_maths',
            'sine = trig_math:sine',
            'linear_math = linear_equations:the_linear_maths',
        ],
    },
)
