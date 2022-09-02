from docplex.mp.model import Model
import numpy as np

# MIP-I
m = Model(name='practice_1')

# parameter
transition_count = 8
place_count = 11
B = 10000
# v ; robot moving time
move_time = 1
# w ; unloading or loading time
load_time = 1

# r_i ; process time
PM1_process_time = 100
PM2_process_time = 200
PM3_process_time = 300

# each PM's process time
process_time = np.array([PM1_process_time, PM2_process_time, PM3_process_time])

# h_l ; each place's holding time
load_move = load_time + move_time
p2_holding_time = load_time + process_time[0]
p5_holding_time = load_time + process_time[1]
p8_holding_time = load_time + process_time[2]
available_place = 0

holding_time = np.array([load_move, p2_holding_time, available_place, load_time, p5_holding_time,
                         available_place, load_time, p8_holding_time, available_place, load_time, available_place])


# P_0 ; the set of nonconflict places
nonconflict_places = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# m0_pl : the number of initial tokens at place pl after the kth firing
m0_place = [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0]

# after kth firing in some firing sequence
# 11 by 1
M_0 = np.array([m0_place]).T


# decision variables

# lambda ; cycle time
z_object = m.continuous_var(name='object_lamda')

# x ; each transition's firing time
x = np.array([])
s = np.array([])
for fire_time_epoch in range(transition_count):
    x_name = 'x' + str(fire_time_epoch + 1)
    s_name = 's' + str(fire_time_epoch + 1)

    x_name = m.continuous_var(lb=0, name=x_name)
    s_name = m.continuous_var(lb=0, name=s_name)

    x = np.append(x, x_name)
    s = np.append(s, s_name)


# z_ki
# z_11 ~ z_88 define
Z_ki = np.array([])

for k in range(transition_count):
    for i in range(transition_count):
        z_name = 'z_' + str(k +1) + str(i+1)
        z_name = m.binary_var(name=z_name)
        Z_ki = np.append(Z_ki, z_name)

Z = Z_ki.reshape(transition_count, -1)

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

# constraint 1
# find x_input, x_output 0 ~ 9, 10 repeat
for p in range(len(nonconflict_places)):
    A_T_index = nonconflict_places[p] - 1
    x_input = np.where(A_T[A_T_index] == 1)[0][0]
    x_output = np.where(A_T[A_T_index] == -1)[0][0]
    m.add_constraint(x[x_output] - x[x_input] >= holding_time[p] - m0_place[p] * z_object)

# constraint 2
for k in range(transition_count):
    z_now = np.array([Z[k]]).T
    if k == 0:
        M_before = M_0

    M_after = M_before + np.dot(A_T, z_now)
    M_before = M_after


# constraint 3, 4
for k in range(transition_count):
    m.add_constraint(np.sum(Z[k]) == 1)
    m.add_constraint(np.sum(Z[:, k]) == 1)

# constraint 5
for k in range(transition_count - 1):
    m.add_constraint(s[k] - s[k+1] <= - (move_time + load_time))

# constraint 6
for k in range(transition_count):
    m.add_constraint(s[k] - (s[0] + z_object) <= - (move_time + load_time))

# constraint 7
for k in range(transition_count):
    for i in range(transition_count):
        m.add_constraint(s[k] - x[i] <= (1 - Z[k][i]) * B)
        m.add_constraint(s[k] - x[i] >= (Z[k][i] - 1) * B)

# object
m.minimize(z_object)

sol = m.solve()
m.print_solution()