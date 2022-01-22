# Full Stack Bootcamp - Unit 01 Lab 16
# Justin Hammond, 01/13/2022

'''
Mini Capstone
For your final Python project, build a program that solves a problem or
accomplishes a task. Your program needs to utilize an external library
(not part of the Python standard library -- this needs to be something
that you pip install).

The functionality of the program is up to you -- use this as an
opportunity to get creative. Sometimes students explore an idea they
want to use for their capstone project or solve an actual problem they
have. For a list of Python libraries to consider using in this project,
check out https://awesome-python.com
'''
from Game import Game
from engine.core.Engine import Engine


def main():
    engine = Engine()
    engine.initialize()
    engine.load_game(Game())
    engine.run()


main()