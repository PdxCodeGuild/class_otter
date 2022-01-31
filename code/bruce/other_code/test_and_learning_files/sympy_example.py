# **************************** #
#        Sympy Example         #
#   sympy subs solve symbols   #
#         Version: 1.0         #
#     Author: Bruce Stull      #
#          2022-01-30          #
# **************************** #

from sympy import symbols, solve

tuple_of_symbols = symbols('x,y,m,x1,y1')
x,y,m,x1,y1 = tuple_of_symbols

# print(f"type(tuple_of_symbols): {type(tuple_of_symbols)}")
# # type(tuple_of_symbols): <class 'tuple'>
# print(f"type(tuple_of_symbols[0]): {type(tuple_of_symbols[0])}")
# # type(tuple_of_symbols[0]): <class 'sympy.core.symbol.Symbol'>

print(f"tuple_of_symbols: {tuple_of_symbols}")
# (x, y, m, x1, y1)

# the_values = (1,2,3,4,5)
# print(the_values)
# # (1, 2, 3, 4, 5)

# tuple_dict = dict(zip(tuple_of_symbols, the_values))
# print(tuple_dict)
# # {x: 1, y: 2, m: 3, x1: 4, y1: 5}

### Method ###
# 1. Make tuple of symbols.
# 2. Make tuple of values.
# 3. Zip symbols and values into a dict.
# 4. Use dict to pass keys and values into function.
# 5. Pass expr into function.
##############


expr = m * (x - x1) + y1 - y


# # Create function to solve equation.
# # Given symbols and equation.
# def linear_solve_ps(the_x=x):
#     print(the_x)

# linear_solve_ps(x)

# ################ Order of logic ################
# # Substitute first, then solve.
# print(expr)
# expr = expr.subs(m, -.5)
# print(expr)
# expr = expr.subs(y1, 1)
# print(expr)
# expr = expr.subs(x1, 1)
# print(expr)
# expr = expr.subs(x, 4)
# print(expr)
# print(round(solve(expr, y)[0], 3))
# ################################################


########### Example ###########
# Solution returned is a list so use sol[n] to get the solution.
print(f"expr: {expr}")
print(f"Equation: [0 = m * (x - x1) + y1 - y]")
for var in tuple_of_symbols:
    sol = solve(expr, var)
    print(f"Solve for {var}: {sol[0]}")
    # print(f"var: {type(var)} : {var}")
# print(f"sol: {type(sol)} : {sol}")

# Solve [0 = m * (x - x1) + y1 - y] for x: (m*x1 + y - y1)/m
# Solve [0 = m * (x - x1) + y1 - y] for y: m*x - m*x1 + y1
# Solve [0 = m * (x - x1) + y1 - y] for m: (y - y1)/(x - x1)
# Solve [0 = m * (x - x1) + y1 - y] for x1: (m*x - y + y1)/m
# Solve [0 = m * (x - x1) + y1 - y] for y1: -m*x + m*x1 + y
# ###############################