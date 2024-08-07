# Write a function make_multiplier_of(n) that takes an integer n and returns a function that multiplies its argument by n. Demonstrate its use with several examples.
def make_multiplier_of(n):
    def multiplies(arg):
        return arg * n
    return multiplies

double = make_multiplier_of(2)
print(double(6))

triple = make_multiplier_of(3)
print(triple(8))