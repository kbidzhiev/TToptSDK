import numpy as np

def function_from_input(input_str):
    def f(x):
        return eval(input_str)
    return f

# Example terminal input string
terminal_input = "np.sum(np.abs(x * np.sin(x) + 0.1 * x))"

# Create the function
f = function_from_input(terminal_input)

# Test the created function
x = np.array([[1, 2], [3, 4]])
result = f(x)
print(result)