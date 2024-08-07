# Create a dictionary with various math functions (e.g., square, cube, square root, factorial). Write a function math_operations(number, operation) that uses this dictionary to apply the requested math function to a number.

import math

math_functions = {'square': lambda x: x ** 2,
                  'cube': lambda x: x ** 3,
                  'square root': lambda x: math.sqrt(x) if x >= 0 else 'It is a negative number',
                  'factorial': lambda x: math.factorial(x) if x >= 0 else 'It is a negative number'}

def math_operations(number, operation):

    if operation in math_functions:
        try:
            return math_functions[operation](number)
        except Exception as e:
            return f'ERROR: {e}'
        
    else:
        return "There is no such operation"
    
print(math_operations(9, 'square'))
print(math_operations(4, 'cube'))
print(math_operations(100, 'square root'))
print(math_operations(5, 'factorial'))
print(math_operations(5, 'fibonacci'))
print(math_operations(-100, 'square root'))