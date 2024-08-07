# Write a function compose(f, g) that returns a new function which is the composition of the functions f and g.
def compose(f, g):
    def my_func(x):
        return f(g(x))
    return my_func

def triple(x):
    return x * 3

def square(m):
    return m ** 2

result = compose(triple, square)
print(result(6))