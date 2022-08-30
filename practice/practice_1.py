from docplex.mp.model import Model
import numpy as np

# MIP-I
m = Model(name='practice_1')

z_object = m.continuous_var(name='object_lamda')

t_in = m.continuous_var(name='input transition')
t_out = m.continuous_var(name='output transition')

h_pl = m.continuous_var(name='the token holding time of place pl')

transition_count = 8
place_count = 11

# m0_pl : the number of initial tokens at place pl
# (11,)
m0_pl = np.array([0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])

# after kth firing in some firing sequence
# 11 by 1
M_0 = np.array([m0_pl]).T

# 1 by 8
z0_i = np.zeros(shape=(1, transition_count), dtype=int)

# Z_k : each transition kth firing
# if transition t_i fires in the kth, zk_i is 1 and otherwise 0
# 8 by 1
Z_0 = z0_i.T

# 11 by 8 |T| x |P|
A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
              [-1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, -1, 1, 1, 0, 0, 0, 0, 0, 0, -1],
              [0, 0, 0, -1, 1, -1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, -1, 1, 1, 0, 0, 0, -1],
              [0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, -1, 1, 1, -1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]])

A_T = A.T

# Constraints
#m.add_constraint(t_out - t_in >= h_pl - m0_pl * z_object)

#for k in range(len(transition_count)):
#    m.add_constraint(np.sum(Z_k) == 1)

# object
#m.minimize(z_object)