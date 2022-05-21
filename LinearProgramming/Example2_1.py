from docplex.mp.model import Model

# Example2.1-1
print("------------Example2.1-1------------")
# create one model instance, with a name
m = Model(name='Example2.1-1')

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
x1 = m.continuous_var(name='Exterior')
x2 = m.continuous_var(name='Interior')

# 1. Exterior paint
# Raw material M1,M2
E_m1 = 6
E_m2 = 1
# Maximum daily availability(tons)
E_max = 24
# Profit Per ton($1000)
E_profit = 5

# 2. Interior paint
# Raw material m1,m2
I_m1 = 4
I_m2 = 2
# Maximum daily availability(tons)
I_max = 6
# Profit Per ton($1000)
I_profit = 4
# Demand Limit
I_limit = 2

# Market Limit
x2_x1 = 1

# write constraints
# constraint_1: Usage of raw material M1 by both paints
m.add_constraint(E_m1 * x1 + I_m1 * x2 <= E_max)
# constraint_2: Usage of raw material M2 by both paints
m.add_constraint(E_m2 * x1 + I_m2 * x2 <= I_max)
# constraint_3: Market limit
m.add_constraint(x2 - x1 <= x2_x1)
# constraint_4: Interior is lesser than 2 ; # Demand limit
m.add_constraint(x2 <= I_limit)

# object
m.maximize(E_profit * x1 + I_profit * x2)

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

# Protein, Fiber

# Corn
corn_p = 0.09
corn_f = 0.02
corn_c = 0.30


# Soybean meal
soy_p = 0.60
soy_f = 0.06
soy_c = 0.90

# at least 800lb of special feed daily.
least = 800
# at least 30% Protein and at most 5% fiber
least_p = 0.3
least_f = 0.05

# write constraints
# constraint_1: at least 800 Ib of special feed daily
m.add_constraint(x1 + x2 >= least)
# constraint_2: requirements of the special feed are at least 30% protein
m.add_constraint(corn_p * x1 + soy_p * x2 >= least_p * (x1+x2))
# constraint_3: requirements of the special feed are at most 5% fiber
m.add_constraint(corn_f * x1 + soy_f * x2 <= least_f * (x1+x2))

# object
m.minimize(corn_c * x1 + soy_c * x2)

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

# Interest rate
Personal_I = 0.140
Car_I = 0.130
Home_I = 0.120
Farm_I = 0.125
Commercial_I = 0.100

# Bad-debt ratio
Personal_B = 0.10
Car_B = 0.07
Home_B = 0.03
Farm_B = 0.05
Commercial_B = 0.02

# loan maximum of $12 million
loan_max = 12
# at least 40% of the funds to farm and commercial loans
least_funds = 0.4
# home loans must equal at least 50% of the personal, car, and home loans
Home_loans = 0.5
# The bank limits the overall ratio of bad debts on all loans to at most 4%
Bank_limit = 0.04

# write constraints
# constraint_1: Total funds should not exceed $12(million)
Total_funds = x1 + x2 + x3 + x4 + x5
m.add_constraint(Total_funds <= loan_max)
# constraint_2: Farm and Commercial loans equal at least 40% of all loans
m.add_constraint(x4 + x5 >= least_funds * Total_funds)
# constraint_3: Home loans should equal at least 50% of personal, car, and home loans
m.add_constraint(x3 >= Home_loans * (x1+x2+x3))
# constraint_4: Bad debts should not exceed 4% of all loans
Bad_debt = Personal_B * x1 + Car_B * x2 + Home_B * x3 + Farm_B * x4 + Commercial_B * x5
m.add_constraint(Bad_debt <= Bank_limit * Total_funds)
Total_Interest = Personal_I * (1-Personal_B) * x1 + Car_I * (1-Car_B) * x2 + Home_I * (1-Home_B) * x3\
                 + Farm_I * (1-Farm_B) * x4 + Commercial_I * (1-Commercial_B) * x5

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

# Interest rate
Personal_I = 0.140
Car_I = 0.130
Home_I = 0.120
Farm_I = 0.125
Commercial_I = 0.100

# Bad-debt ratio
Personal_B = 0.10
Car_B = 0.07
Home_B = 0.03
Farm_B = 0.05
Commercial_B = 0.02

# Personal, Car, Home, Farm, Commercial
x = np.array([x1, x2, x3, x4, x5])
Inter = np.array([Personal_I, Car_I, Home_I, Farm_I, Commercial_I])
Bad = np.array([Personal_B, Car_B, Home_B, Farm_B, Commercial_B])
good = 1-Bad
rate = Inter * good
Total_Interest = np.sum(x * rate)
Bad_debt = np.sum(Bad * x)

# loan maximum of $12 million
loan_max = 12
# at least 40% of the funds to farm and commercial loans
least_funds = 0.4
# home loans must equal at least 50% of the personal, car, and home loans
Home_loans = 0.5
# The bank limits the overall ratio of bad debts on all loans to at most 4%
Bank_limit = 0.04

# constraint
m.add_constraint(np.sum(x) <= loan_max)
m.add_constraint(x[3]+x[4] >= least_funds * np.sum(x))
m.add_constraint(x[2] >= Home_loans * (x[0]+x[1]+x[2]))
m.add_constraint(Bad_debt <= Bank_limit * np.sum(x))

# object
m.maximize(Total_Interest - Bad_debt)

s = m.solve()
m.print_solution()