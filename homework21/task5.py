# Implement a function power_factory(n) that returns a function which raises its argument to the power of n.
def power_factory(n):
    def argument(m):
        return m ** n
    return argument

result = power_factory(2)
print(result(5))