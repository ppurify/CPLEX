import scipy.optimize as so
import numpy as np

# Example2.1-1
A = np.array([[6, 4], [1, 2], [-1, 1], [0, 1]])
b = np.array([24, 6, 1, 2])
c = np.array([-5, -4])

result = so.linprog(c, A, b, method='simplex')
print(result)

# Example2.2-2
# A = np.array([[1, 2], [0.21, -0.3], [0.03, -0.01]])
# b = np.array([800, 0, 0, 0])
# c = np.array([0.3, 0.9])
#
# result = so.linprog(c, A, b, method='simplex')
# print(result)