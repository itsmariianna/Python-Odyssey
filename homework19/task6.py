# Create a function named apply_function that takes an iterable and a function, and applies the function to each element of the iterable, returning a list of the results.

def apply_function(func, iterable):
    ls = []
    for i in iterable:
        n = func(i)
        ls.append(n)
    return ls

my_ls = [1, 2, 3, 4, 5]
my_func = lambda x : x ** 2
print(apply_function(my_func, my_ls))





































