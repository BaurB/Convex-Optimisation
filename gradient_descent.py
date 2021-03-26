import numpy as np
import matplotlib.pyplot as plt 

# Gradient Descent
def gradient_descent(f, f_prime, start, learning_rate = 0.1):
    initial_x = start
    iterations = 50
    for i in range(iterations):
        x = initial_x - learning_rate * f_prime(initial_x)
        initial_x = x
    return x
    
    
f = lambda x : (x - 1) ** 4 + x ** 2    
f_prime = lambda x : 4*((x-1)**3) + 2*x

start = -1

x_min = gradient_descent(f, f_prime, start, learning_rate = 0.1)
f_min = f(x_min)
# print("xmin: %0.2f, f(x_min): %0.2f" % (x_min, f_min)) # Uncomment to see the result

# Plot figure
x = np.linspace(x_min - 1, x_min + 1, 100)
y = [f(val) for val in x]
plt.plot(x, y, color='blue', label='f')

# plot optima
plt.scatter(x_min, f(x_min), color='red', marker='x', label='Minimum')

plt.grid()
plt.legend(loc = 3) # print('x_min: %.02f' % (res))


''' Small learning rate results in longer time required in finding the minimum point of a function
 High learning rate increases the risk of 'missing' the global minimum of a function
 ---------------------------------------------------------------------------------------------------------------------
'''


