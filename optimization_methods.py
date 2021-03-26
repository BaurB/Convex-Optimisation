import matplotlib.pyplot as plt
import numpy as np

# Plot a given function across an interval (to see how it behaves)

def f(x):
    return ((x - 1)**4 + x**2)

x = np.linspace(-0.5,0.75,50)
plt.plot(x, f(x))
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()

# Writing a simple bisection method algorithm to find a point where a function is minimum 



def f(x):
    return ((x - 1)**4 + x**2)

def f(x):
    return ((x - 1)**4 - x**2)  

# def bisection (a, b, tol):
#     xl = a
#     xr = b
#     while (np.abs(xl -xr) >= tol):
#         c = (xl + xr)/2.0
#         prod = f(xl) * f(c)
#         if prod > tol:
#             xl = c
#         else:
#             if prod < tol:
#                 xr = c
#     return c 

# print(bisection(-2, 2, 1e-8))

# Bisection method is an iterative method of finding local minimum of function through introduction of central point which is half the distance of left and right boundaries
def find_root(f, a, b, tolerance):
    left_boundary = a
    right_boundary = b
    while (np.abs(left_boundary - right_boundary) >= tolerance):
        centre = (left_boundary + right_boundary)/2.0
        product = f(left_boundary) * f(centre)
        if (product > tolerance):
            left_boundary = centre
        elif (product < tolerance):
            right_boundary = centre
    return centre

print('x_min:', find_root(f, -5, 5, 1e-10)) # Based on bisection method, f(x) is minimum at x =  0.3819608689082088

            
        
# Using find_root to find the root of f prime.

def f_prime(x):
    return 4 * (x - 1)**3 + 2 * x

print('x_min::',find_root(f_prime, -10, 10, 1e-10)) # Based on bisection method, f_prime(x) is minimum at x = 0.41024446494702715



# I used two optimization methods available from sklearn to check if the result from biscetion method is accurate. The used optimization methods are Newton Raphson and Brent Optimization 

# Newton Raphson Method
from scipy.optimize import newton

f = lambda x : (x - 1)**4 + x**2

res = newton(f, 1, maxiter = 100000)
print('Newton Raphson Method -> x_min: %.02f, f(x_min): %.02f' % (res, f(res)))

x = np.linspace(res - 1, res + 1, 100)
y = [f(val) for val in x]
plt.plot(x, y, color='blue', label='f')

# plot optima
plt.scatter(res, f(res), color='red', marker='x', label='Minimum')

plt.grid()
plt.legend(loc = 3)


# Brent Optimization
from scipy.optimize import minimize_scalar

res = minimize_scalar(f, method='brent')
print('Brent Optimization -> x_min: %.02f, f(x_min): %.02f' % (res.x, res.fun))

# plot curve
x = np.linspace(res.x - 1, res.x + 1, 100)
y = [f(val) for val in x]
plt.plot(x, y, color='blue', label='f')

# plot optima
plt.scatter(res.x, res.fun, color='red', marker='x', label='Minimum')

plt.grid()
plt.legend(loc = 3)



''' Conclusion/Observation: We can see that the bisection method gives different result whether you use original function or it's derivative. Brent and Newton raphson optimization technique gives slightly different results
Also, the use of bisection method on derivative of a function give nearly the same result as a Newton Raphson Methods'''