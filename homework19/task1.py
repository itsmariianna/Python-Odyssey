# Create a Python function named my_map that mimics the behavior of Python’s built-in map() function. The function should take a function and an iterable, apply the function to each item in the iterable, and return a list of the results.
# Requirements:
# Return a list of results instead of using a generator.
# Include type annotations and a detailed docstring explaining how the function works.
# Do not use the built-in map() in your implementation.


def my_map(func, iterable) :

    """
    Apply a function to each item in an iterable and return a list of the results.

    Parameters:
    func: function that takes an element and returns a value.
    iterable: An iterable containing elements.

    Returns:
    List: A list containing the results of applying the function to each item in the iterable.

    """

    result = [func(item) for item in iterable]
    return result

def square(x: int) -> int:
    return x ** 2

ls = [1, 2, 3, 4, 5]

result = my_map(square, ls)
print(result)
