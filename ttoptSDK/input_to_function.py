def function_from_input(input_str):
    def f(x):
        return eval(input_str)
    return f