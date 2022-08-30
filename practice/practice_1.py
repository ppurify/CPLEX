from docplex.mp.model import Model
import numpy as np

# MIP-I
m = Model(name='practice_1')

# parameter
transition_count = 8
place_count = 11

# v ; robot moving time
move_time = 1
# w ; unloading or loading time
load_time = 1

# r_i ; process time
PM1_process_time = 100
PM2_process_time = 200
PM3_process_time = 300

# decision variables

# lambda ; cycle time
z_object = m.continuous_var(name='object_lamda')

# x ; each transition's firing time
x1 = m.continuous_var(lb=0, name='x1 firing time')
x2 = m.continuous_var(lb=0, name='x2 firing time')
x3 = m.continuous_var(lb=0, name='x3 firing time')
x4 = m.continuous_var(lb=0, name='x4 firing time')
x5 = m.continuous_var(lb=0, name='x5 firing time')
x6 = m.continuous_var(lb=0, name='x6 firing time')
x7 = m.continuous_var(lb=0, name='x7 firing time')
x8 = m.continuous_var(lb=0, name='x8 firing time')
x = np.array([x1, x2, x3, x4, x5, x6, x7, x8])

for k in range(transition_count):



# each PM's process time
process_time = np.array([PM1_process_time, PM2_process_time, PM3_process_time])

# h_l ; each place's holding time
load_move = load_time + move_time
p2_holding_time = load_time + process_time[0]
p5_holding_time = load_time + process_time[1]
p8_holding_time = load_time + process_time[2]
avaliable_place = 0

holding_time = np.array([load_move, p2_holding_time, avaliable_place, load_time, p5_holding_time,
                         avaliable_place, load_time, p8_holding_time, avaliable_place, load_time, avaliable_place])


# P_0 ; the set of nonconflict places
nonconflict_places = np.array([1,2,3,4,5,6,7,8,9,10])

# m0_pl : the number of initial tokens at place pl after the kth firing
# (11,)
m0_place = np.array([0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])

# after kth firing in some firing sequence
# 11 by 1
M_0 = np.array([m0_place]).T

# 1 by 8
# Z_k : each transition kth firing
# if transition t_i fires in the kth, zk_i is 1 and otherwise 0


# A : |T| x |P|
A = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
              [-1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, -1, 1, 1, 0, 0, 0, 0, 0, 0, -1],
              [0, 0, 0, -1, 1, -1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, -1, 1, 1, 0, 0, 0, -1],
              [0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, -1, 1, 1, -1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]])
# A_T : 11 by 8
A_T = A.T
# print('A_T : ', A_T.shape)
# print(A_T)

# constraint 1
# find x_input, x_output
# for p in range(len(nonconflict_places)):
#     A_T_index = nonconflict_places[p] - 1
#     # print(A_T_index)
#     x_input = np.where(A_T[A_T_index] == 1)[0][0]
#     x_output = np.where(A_T[A_T_index] == -1)[0][0]
#     m.add_constraint(x[x_output] - x[x_input] >= holding_time[p] - m0_place * z_object)

#for k in range(transition_count):
#    if k == 0:
#        M_before = M_0

#    else:
#        M_before = M_new

    #M_new = M_before + A_T * Z_k

for k in range(transition_count):




# object
#m.minimize(z_object)