from ttoptSDK.input_to_function import function_from_input
import numpy as np

def isclose(x, y, tol=1e-10):
    return abs(x - y) < tol

def test_function_from_input():
    input_str = "np.sin(x)"
    f = function_from_input(input_str)
    assert isclose(f(0), 0)
    assert isclose(f(np.pi/2), 1)
    assert isclose(f(np.pi/4), 1/np.sqrt(2))
    assert not isclose(f(0), 0.1)


