from ttopt import TTOpt

def optimize(
    rank,
    d,
    f,
    lower_grid_bound,
    upper_grid_bound,
    p_grid_factor,
    q_grid_factor,
    n_evals,
    x_opt_real=None,
    y_opt_real=None,
    name='Alpine',
    with_log=False,
    ):

    tto = TTOpt(
    f=f,
    d=d,
    a=lower_grid_bound,
    b=upper_grid_bound,
    p=p_grid_factor,
    q=q_grid_factor,
    evals=n_evals,
    x_opt_real=x_opt_real,
    y_opt_real=y_opt_real,
    name=name,
    with_log=with_log)

    tto.optimize(rank)

    x_min = tto.x_opt
    y_min = tto.y_opt
    n_chache_usage = tto.k_cache
    t_average = tto.t_evals_mean

    assert tto.k_evals == n_evals
    total = tto.info()

    return x_min, y_min, (n_chache_usage, t_average, total)
