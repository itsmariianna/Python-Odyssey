# Write a function make_accumulator(start=0) that returns a function which adds its argument to start and returns the new total each time it is called.

def make_accumulator(start=0):
    def inner(value):
        nonlocal start
        start += value
        return start
    return inner

result = make_accumulator(10)
print(result(1))
print(result(2))
print(result(3))




