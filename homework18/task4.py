# Write a function to process data with different operations.
# Use positional-only arguments for data (list of numbers).
# Use a keyword argument for the operation (default is ‘sum’).
# Return the result of the operation.

def data_operations(*args, operation = 'sum'):
    if operation == 'sum':
        return f'Sum is {sum(args)}'
    elif operation == 'product':
        count = 1
        for i in args:
            count *= i
        return f'Product is {count}'
    elif operation == 'mean':
        return f'Mean is {sum(args) / len(args)}'
    else:
        return f'There is no {operation} operation. Try sum, product or mean'
    
my_list = [1, 2, 3, 4, 5]
result = data_operations(*my_list, operation='mean')
print(result)