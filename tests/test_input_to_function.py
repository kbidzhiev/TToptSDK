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

    input_str = "np.sin(x) + 0.1"
    f = function_from_input(input_str)
    assert isclose(f(0), 0.1)
    assert isclose(f(np.pi/2), 1.1)
    assert isclose(f(np.pi/4), 1/np.sqrt(2)+0.1)
    assert not isclose(f(0), 0)

    input_str = "np.sum(np.abs(x * np.sin(x) + 0.1 * x))"
    f = function_from_input(input_str)
    x = np.array([[1, 2], [3, 4]])
    assert isclose(f(x), 6.310635843870575)



