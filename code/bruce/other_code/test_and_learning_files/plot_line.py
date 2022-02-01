

import matplotlib.pyplot as plt
import numpy as np
import math

def plot_a_line(slope, ex, wye, ux, uy):
    m = slope
    x1 = ex
    y1 = wye
    line_label = f"{m} * (x - {x1}) + {y1}"

    x = np.linspace(-5, 5, 100)
    y = m * (x - x1) + y1
    fig, ax = plt.subplots()
    ax.plot(ux, uy, 'go', label='User Point')
    ax.plot(x, y, label=line_label)
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # loc= 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    plt.legend(loc='best', shadow=True)
    plt.show()


m = .5
x1 = 1
y1 = 1
userx = 1
usery = 1 
plot_a_line(m,x1,y1,userx,usery)



# x = np.linspace(-10.0, 10.0, num=100)
# print(x)
# plt.plot(x, np.sin(x), label="sin(x)")
# y: m*x - m*x1 + y1


# ##### Test a line #####
# # x = np.array([1,2,3,4])  # Optional way to set x.
# x = np.linspace(-10.0, 10.0, num=100)
# y = x * .5 + 3
# plt.plot(x, y, label="x * .5 + 3")
# #######################


# ##### Test a line #####
# m = -.5
# x1 = 1
# y1 = 1
# line_label = f"{m} * (x - {x1}) + {y1}"

# x = np.linspace(-10.0, 10.0, num=100)
# y = m * (x - x1) + y1
# fig, ax = plt.subplots()
# ax.plot(x, y, label=line_label)

# #######################


# ##### Online example #####
# # This works well
# x = np.linspace(0.2,10,100)
# fig, ax = plt.subplots()
# ax.plot(x, 1/x)
# ax.plot(x, np.log(x))
# ax.set_aspect('equal')
# ax.grid(True, which='both')

# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# ##########################
