from docplex.mp.model import Model

# Example2.1-1
print("------------Example2.1-1------------")
# create one model instance, with a name
m = Model(name='Example2.1-1')

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
x1 = m.continuous_var(name='Exterior')
x2 = m.continuous_var(name='Interior')

# write constraints
# constraint_1: Usage of raw material M1 by both paints
m.add_constraint(6 * x1 + 4 * x2 <= 24)
# constraint_2: Usage of raw material M2 by both paints
m.add_constraint(x1 + 2 * x2 <= 6)
# constraint_3: Market limit
m.add_constraint( x2 -x1  <= 1)
# constraint_4: Interior is lesser than 2 ; # Demand limit
m.add_constraint(x2 <= 2)

# object
m.maximize(5 * x1 + 4 * x2)

# Print information about the model
# m.print_information()

# Solve with the model
s = m.solve()
m.print_solution()


# Example2.2-2
print("\n------------Example2.2-2------------")
# create one model instance, with a name
m = Model(name='Example2.2-2')

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
x1 = m.continuous_var(name='Corn')
x2 = m.continuous_var(name='Soybean meal')

# write constraints
# constraint_1: at least 800 Ib of special feed daily
m.add_constraint(x1 + x2 >= 800)
# constraint_2: requirements of the special feed are at least 30% protein
m.add_constraint(0.09 * x1 + 0.6 * x2 >= 0.3 * (x1+x2))
# constraint_3: requirements of the special feed are at most 5% fiber
m.add_constraint(0.02 * x1 + 0.06 * x2 <= 0.05 * (x1+x2))

# object
m.minimize(0.3 * x1 + 0.9 * x2)

# Print information about the model
# m2.print_information()

# Solve with the model
s = m.solve()
# if s is None:
#     print('- model is infeasible')
m.print_solution()


# Example2.4-1
print("\n------------Example2.4-1------------")
# create one model instance, with a name
m = Model(name='Example2.4-1')

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
x1 = m.continuous_var(name='Personal')
x2 = m.continuous_var(name='Car')
x3 = m.continuous_var(name='Home')
x4 = m.continuous_var(name='Farm')
x5 = m.continuous_var(name='Commercial')

# write constraints
# constraint_1: Total funds should not exceed $12(million)
Total_funds = x1 + x2 + x3 + x4 + x5
m.add_constraint(Total_funds <=12)
# constraint_2: Farm and Commercial loans equal at least 40% of all loans
m.add_constraint(x4 + x5 >= 0.4 * Total_funds)
# constraint_3: Home loans should equal at least 50% of personal, car, and home loans
m.add_constraint(x3 >= 0.5 * (x1+x2+x3))
# constraint_4: Bad debts should not exceed 4% of all loans
Bad_debt = 0.1 * x1 + 0.07 * x2 + 0.03 * x3 + 0.05 * x4 + 0.02 * x5
m.add_constraint(Bad_debt <= 0.04 * Total_funds)
Total_Interest = 0.14 * 0.9 * x1 + 0.13 * 0.93 * x2 + 0.12 * 0.97 * x3 + 0.125 * 0.95 * x4 + 0.1 * 0.98 * x5

# object : Total Interest - Bad debt
m.maximize(Total_Interest - Bad_debt)

# Print information about the model
# m2.print_information()

# Solve with the model
s = m.solve()
# if s is None:
#     print('- model is infeasible')
m.print_solution()
# 출력되지 않은 변수들은 0이라서 나타나지 않았음!

print("\n-----Example2.4-1 other way-----")
import numpy as np
# Model
m = Model(name='Practice')

x1 = m.continuous_var(name='Personal')
x2 = m.continuous_var(name='Car')
x3 = m.continuous_var(name='Home')
x4 = m.continuous_var(name='Farm')
x5 = m.continuous_var(name='Commercial')

x = np.array([x1,x2,x3,x4,x5])
Inter = np.array([0.14, 0.13, 0.12, 0.125, 0.1])
Bad = np.array([0.1, 0.07, 0.03, 0.05, 0.02])
good = 1-Bad
rate = Inter * good
Total_Interest = np.sum(x * rate)
Bad_debt = np.sum(Bad * x)

# constraint
m.add_constraint(np.sum(x) <= 12)
m.add_constraint(x[3]+x[4] >= 0.4 * np.sum(x))
m.add_constraint(x[2] >= 0.5 * (x[0]+x[1]+x[2]))
m.add_constraint(Bad_debt <= 0.04 * np.sum(x))

# object
m.maximize(Total_Interest - Bad_debt)

s = m.solve()
m.print_solution()