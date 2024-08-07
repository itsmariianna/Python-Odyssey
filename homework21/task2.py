# Write a function make_adder(n) that returns a function that adds n to its argument.
def make_adder(n):
    def argument(m):
        return n + m
    return argument

result = make_adder(7)
print(result(9))