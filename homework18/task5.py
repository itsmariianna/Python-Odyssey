# Write a function to display product details by unpacking a dictionary.
# Use unpacking to pass product details as keyword arguments to the function.

def product_details(name, writer, price):
    return f'Book details\nName: {name}\nWriter: {writer}\nPrice: {price}'

my_dict = {'name':'Atomic Habits', 'writer':'James Clear', 'price':30}
result = product_details(**my_dict)
print(result)