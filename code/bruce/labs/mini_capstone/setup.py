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
        # pipenv install -e .
            # It seems we need to reinstall when editing function names.
    # https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used
        # https://pipenv-fork.readthedocs.io/en/latest/basics.html#specifying-versions-of-a-package

from setuptools import setup

setup(
    name='butterscotch-pi',
    version='0.1.0',
    py_modules=[
        # 'strings',
        # 'basic_math',
        # 'trig_math',
        # 'linear_math',
        ],
    package_dir = {'': 'the_logic'},
    install_requires=[
        'click',
        'sympy',
        'matplotlib',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            # Greetings and strings.
            'hello = strings:greeting',

            # Commands to get to the module/page.
            'basic_math = basic_math:the_maths',
            'trig_math = trig_math:the_trig_maths',
            'linear_math = linear_math:the_linear_maths',

            # Commands to get to the specific function.
            'add = basic_math:add',
            'subtract = basic_math:subtract',
            'multiply = basic_math:multiply',
            'divide = basic_math:divide',
            'factorial = basic_math:factorial',
            'inverse = basic_math:inverse',
            'sqroot = basic_math:sqroot',
            'nth_power = basic_math:nth_power',
            'log = basic_math:log',

            # Trigonometric calculations.
            'sine = trig_math:sine',
            'cosine = trig_math:cosine',
            'tan = trig_math:tan',

            # Linear equations.
            'linear_ps = linear_math:linear_ps',
            'linear_si = linear_math:linear_si',
            'linear_pp = linear_math:linear_pp',
        ],
    },
)
