# Create a decorator that validates the input arguments of a function (e.g., ensures all arguments are positive integers). Apply this decorator to a function that performs mathematical operations.

def positive_integers(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) and arg > 0 for arg in args) and all(isinstance(i, int) and i > 0 for i in kwargs.values()):
            result = func(*args, **kwargs)
            return f'Everything is okay. Result is: {result}'
        else:
            return "This function works only for positive integers"
    return wrapper

@positive_integers
def my_func(a, b, *, c):
    return a + b + c

print(my_func(4, 6, c = 7))
print(my_func(4, 6, c = -6))
print(my_func(4, -6, c = 6))