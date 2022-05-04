import scipy.optimize as so
import numpy as np

A = np.array([[6, 4], [1, 2], [-1, 1], [0, 1]])
b = np.array([24, 6, 1, 2])
c = np.array([-5, -4])

result = so.linprog(c, A, b, method='simplex')
print(result)
print("HI")