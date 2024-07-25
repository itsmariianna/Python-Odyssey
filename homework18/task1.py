# Create a function to greet a user with their full name and a custom message.
# Use positional arguments for first name and last name.
# Use a keyword argument for the greeting message with a default value.

def greeting(name, surname, message = 'Hello, '):
    return f'{message} {name} {surname}'

n = input("Enter name: ")
s = input("Enter surname: ")
m = input("Enter message: ")
print(greeting(n, s))
print(greeting(n, s, m))