# Store functions for common list transformations (e.g., sorting, reversing, filtering, mapping) in a dictionary. Write a function transform_list(lst, operation) that uses this dictionary to perform the requested transformation on a list.

transformations = {'sorting': lambda lst: sorted(lst),
                   'reversing': lambda lst: lst[::-1],
                   'filtering': lambda lst: list(filter(lambda x: x % 2 == 0, lst)),
                   'mapping': lambda lst: list(map(lambda x: x**2, lst))}

def transform_list(lst, operation):

    if not lst:
        return "List is empty"
    elif operation in transformations:
        try:
            return transformations[operation](lst)
        except Exception as e:
            return f'ERROR: {e}'
    else:
        return "There is no such transformation"

print(transform_list([8, 7, 4, 0, 1], 'sorting'))
print(transform_list([8, 7, 4, 0, 1], 'reversing'))
print(transform_list([1, 2, 3, 4, 5, 6], 'filtering'))
print(transform_list([1, 2, 3, 4, 5, 6], 'mapping'))
print(transform_list([1, 2, 3, 4, 5, 6], 'lenght'))
print(transform_list([1, 2, 3, 4, 5, 'hello'], 'mapping'))