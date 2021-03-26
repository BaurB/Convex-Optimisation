# To go Further - Simplex Algorithm for Linear Programming

from scipy.optimize import linprog
import numpy as np
A = np.array([[2, 1], [-4, 5], [1, -2]])
b = np.array([10, 8, 3])
c = np.array([1,2])

def solve_linear_problem(A, b, c):
    c *= -1
    x_bounds= (0, None)
    y_bounds = (0, None)
    res = linprog(c, A, b, method = 'simplex')
    return (res)

optimal_value= solve_linear_problem(A, b, c)
# print(optimal_value) 

# A key insight is that the optimal solution to any constrained linear optimization problem is always on one of the corners of the convex polytope. It could be seen by plotting a graph


# Implementation of Simplex Algorithm from scratch
from simplex_implementation import generate_matrix
from simplex_implementation import constrain
from simplex_implementation import constrain
from simplex_implementation import obj
from simplex_implementation import maxz

table = generate_matrix(2,3)
constrain(table, '2,1,L,10' ) # 2x + y <= 10
constrain(table,'-4,5,L,8') # -4x + 5y <= 8
constrain(table,'1,-2,L,3') # x - 2y <= 3
obj(table,'1,2,0') # z = x + 2y
print(maxz(table)) # Maximising the function

