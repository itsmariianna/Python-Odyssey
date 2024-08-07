# Create a function make_counter() that returns a function that, when called, increments and returns a counter variable. The counter should start at 0 and increment by 1 each time the function is called.

def make_counter():
    count = 0
    def func():
        nonlocal count
        result = count
        count += 1
        return result
    return func

my_func = make_counter()
print(my_func())
print(my_func())
print(my_func())
print(my_func())