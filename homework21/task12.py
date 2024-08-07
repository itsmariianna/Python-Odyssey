# Implement a function make_memoize(f) that takes a function f and returns a memoized version of f which caches results to avoid redundant computations.
def make_memoize(f):
    cache = {}
    
    def memoized(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    
    return memoized

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = make_memoize(fibonacci)

print(result(8))
print(result(18))
