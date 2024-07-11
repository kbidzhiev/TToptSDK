from ttoptSDK.sdk import optimize
import numpy as np

np.random.seed(42)

def isclose(x, y, tol=1e-10):
    return abs(x - y) < tol

def optimise_input_function(f, d):
    rank = 4
    lower_grid_bound = -10
    upper_grid_bound = 10
    p_grid_factor = 2
    q_grid_factor = 12
    n_evals = 2 * 1.E+3

    x_opt_real=np.ones(d)
    y_opt_real=0.

    x, y, info = optimize(rank,
             d,
             f,
             lower_grid_bound,
             upper_grid_bound,
             p_grid_factor,
             q_grid_factor,
             n_evals,
             x_opt_real,
             y_opt_real,
             with_log=False
             )
    return x, y

def test_optimise_1():
    def f(X):
        return np.sum(np.abs(X * np.sin(X) + 0.1 * X), axis=1)
    
    d = 2
    x, y = optimise_input_function(f, d)
    
    assert isclose(y, 9.029805474642522e-06)
    assert isclose(x[0], -0.10012210012209977)
    assert isclose(x[1], -0.10012210012209977)

def test_optimise_2():
    def f(X):
        return np.sum(X**3 - 2 * X, axis=1)
    
    d = 3
    x, y = optimise_input_function(f, d)
    
    assert isclose(y, -2940)
    assert isclose(x[0], -10)
    assert isclose(x[1], -10)
    assert isclose(x[2], -10)

