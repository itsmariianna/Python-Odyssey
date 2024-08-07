# Create a function apply_twice(f, x) that applies a given function f to an argument x two times.
def apply_twice(f, x):
    return f(f(x))

def double(num):
    return num * 2

print(apply_twice(double, 6))
