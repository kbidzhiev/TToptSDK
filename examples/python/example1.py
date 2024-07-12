from ttoptSDK import optimize
import numpy as np



def f(X):
    return np.sum(X**3 - 2 * X, axis=1)

d = 3
rank = 4
lower_grid_bound = -10
upper_grid_bound = 10
p_grid_factor = 2
q_grid_factor = 12
n_evals = 2 * 1.E+3
name = "myfunc"
with_log = True
x_opt_real=np.ones(d)
y_opt_real=0.




x, y, info = optimize(rank, d, f,
         lower_grid_bound, upper_grid_bound,
         p_grid_factor, q_grid_factor,
         n_evals,
         #name, with_log,
         #x_opt_real, y_opt_real,
         )

print(f"x_min = {x}")
print(f"y_min = {y}")