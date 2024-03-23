import math
import matplotlib.pyplot as plotter
from numpy import array, linspace
# Machine epsilon can be calculated as the ULP of 1.0
machine_epsilon = math.ulp(100)

def linear(x):
    return array([x1 for x1 in x])
def squared(x):
    return array([x1**2 for x1 in x])
def sine(x):
    return array([math.sin(x1) for x1 in x])
def derivative(x,y,a = machine_epsilon):
    return (x-y)/a
x1 = linspace(-10,10,100000)
func_lin = linear(x1)
func_squared = squared(x1)
func_sine = sine(x1)

diff_linear = derivative(linear(x1+machine_epsilon),func_lin)
diff_squared = derivative(squared(x1+machine_epsilon),func_squared)
diff_sine = derivative(sine(x1+machine_epsilon),func_sine)

fig, ax = plotter.subplots()
ax.plot(x1,func_lin)
ax.plot(x1,diff_linear)
ax.plot(x1,func_squared)
ax.plot(x1,diff_squared)
ax.plot(x1,func_sine)
ax.plot(x1,diff_sine)
ax.set_xlim(-5,5)
ax.set_ylim(-4,4)
ax.grid(True)
plotter.show()
