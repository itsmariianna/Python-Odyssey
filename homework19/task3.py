# Develop a function called my_zip that combines elements from multiple iterables into tuples, similar to the built-in zip() function, and returns a list of these tuples.
# Requirements:
# The function should stop zipping when the shortest iterable is exhausted and return a list of tuples.
# Include type annotations and a detailed docstring.
# Do not use the built-in zip() in your code.


def my_zip(*iterables):

    """
    Combine elements from multiple iterables into tuples, stopping when the shortest iterable is exhausted.

    Parameters:
    *iterables: Multiple iterables of elements combined into tuples.

    Returns:
    List: A list of tuples, where each tuple contains elements from the input iterables at the same index.

    """

    ls = []
    shortest = len(iterables[0])
    for i in iterables:
        if len(i) < shortest:
            shortest = len(i)

    for i in range(shortest):
        result = []
        for j in iterables:
            result.append(j[i])
        ls.append(tuple(result))
    return ls

ls1 = [1, 2, 3]
ls2 = [6, 7, 8, 9]
ls3 = [10, 11, 12]

print(my_zip(ls1, ls2, ls3))
