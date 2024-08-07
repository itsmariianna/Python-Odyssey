# Create a function named get_nth_element that takes an iterable and an integer n, and returns the n-th element from the iterable using iter() and next().

def get_nth_element(iterable, n):
    iterator = iter(iterable)
    
    try:
        for _ in range(n):
            next_element = next(iterator)
        return next_element
    
    except StopIteration:
        return "Error"

ls = [11, 22, 33, 44, 55, 66]
element = 3
print(get_nth_element(ls, element))

















