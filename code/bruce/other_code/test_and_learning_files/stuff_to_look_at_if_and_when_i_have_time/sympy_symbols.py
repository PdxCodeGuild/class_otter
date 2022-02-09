# **************************** #
#        Sympy Symbols         #
#   sympy subs solve symbols   #
#         Version: 1.0         #
#     Author: Bruce Stull      #
#          2022-01-31          #
# **************************** #

# Use symbols(), and solve() to create some symbols and then solve equations.

# Import some sympy methods.
# Use expr.<method> to access the methods.
from sympy import symbols, solve

print('###############')
x, y = symbols('x y')
print(f"symbols('x y'): {symbols('x y')}")
print(f"type(symbols('x y')): {type(symbols('x y'))}")
print(f"x: {type(x)}")

expr = x + 5
print(f'type(expr): {type(expr)}')
sol = solve(expr, x)
print(f"type(sol): {type(sol)}")
x = sol[0]
print(f"type(x): {type(x)}")

# Since we are only displaying the result and not processing it further,
# it is okay to display the value, even though it is not a
# literal 'int' or 'float'.
print(f"type(x.subs(x,2)): {type(x.subs(x,2))}")



print('###############')
# Work with two symbols, 'x' and 'y'.
# Two ways to create the symbols, with ' ' or ',' in argument.

# Use a space ' ' or comma ',' delimited string:
x, y = symbols('x y')

# print(f"type(symbols('x y')): {type(symbols('x y'))}")
# print(f"type(x): {type(x)}")
# # type(symbols('x y')): <class 'tuple'>
# # type(x): <class 'sympy.core.symbol.Symbol'>

# x, y = symbols('x,y')
# print(f"x, y = symbols('x,y') - type(x): {type(x)}")

# Solve y = 5 * x + 3, for y:
expr1 = -y + 5 * x + 3
# Use solve(), which returns a list.
sol1 = solve(expr1, y)

# TODO: Understand when sol[] would have more than one element.
# for sol in sol1:
#     print(f"{type(sol)} : {sol}")
# <class 'sympy.core.add.Add'> : 5*x + 3

# Use sol1[0] to get the first element, which is the solution.
print(sol1[0])
# 5*x + 3

# # Solve y = 5 * x + 3, for x:
expr2 = -y + 5 * x + 3
sol2 = solve(expr2, x)
print(sol2[0])
# y/5 - 3/5