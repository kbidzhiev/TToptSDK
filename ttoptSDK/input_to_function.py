import numpy as np #input functions from `input_str` are base on numpy

def function_from_input(input_str):
    def f(X):
        return eval(input_str)
    return f