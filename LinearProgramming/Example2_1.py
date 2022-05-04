from docplex.mp.model import Model

# create one model instance, with a name
m = Model(name='Practice1')

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

m.maximize(5 * x1 + 4 * x2)

# Print information about the model
# m.print_information()

# Solve with the model
s = m.solve()
m.print_solution()

# Example2.2-2
