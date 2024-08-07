# Create a function named my_filter that behaves like Python’s built-in filter() function. It should filter items out of an iterable based on a function that returns either True or False and return a list of the filtered items.
# Requirements:
# Return a list of filtered items instead of using a generator.
# Include type annotations and a detailed docstring.
# Avoid using the built-in filter() in your implementation.

def my_filter(function, iterable):

    """
    Filter items from an iterable based on a function that returns True or False.

    Parameters:
    func: A function that takes an element and returns a boolean value.
    iterable: An iterable containing elements.

    Returns:
    List: A list of items from the iterable for which the function returns True.

    """


    ls = [i for i in iterable if function(i)]
    return ls

def even(x: int) -> int:
    if x % 2 == 0:
        return True
    return False

my_list = [1, 2, 3, 4, 5, 6]
result = my_filter(even, my_list)

print(result)
