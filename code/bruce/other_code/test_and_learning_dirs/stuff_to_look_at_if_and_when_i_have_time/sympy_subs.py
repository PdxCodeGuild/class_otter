# **************************** #
#      Sympy Substitution      #
#   sympy subs solve symbols   #
#         Version: 1.0         #
#     Author: Bruce Stull      #
#          2022-01-31          #
# **************************** #

# Use symbols(), solve(), and subs().
    # Create symbols():
    # solve() equations which contain those symbols:
    # Express results with subs() of those symbols:

# Import some sympy methods.
# Will will use expr.<method>.
from sympy import symbols, solve

# Create the symbols for linear equation:
x, y = symbols('x,y')
# Solve isn't neccessary right now since we have y = f(x).
# y = -.5 x + 3
# 1. Create expression of form 0 = g(z):
expr1 = -y + -.5 * x + 3
# 2. Solve expr for desired symbol:
sol_list = solve(expr1, y)
# 3. Get the solution expression:
sol_y = sol_list[0]
# 4. Substitute a value:
sol_1 = sol_y.subs(x, 3)
# 5. Print the result:
print(f"{type(sol_1)} : {sol_1}")
print(f"{type(float(sol_1))} : {float(sol_1)}")