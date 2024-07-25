# Create a function that updates user settings by passing keyword arguments dynamically.
# Use **kwargs to accept dynamic user settings.
# Use a function to pass these settings as keyword arguments to another function.

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


my_dict = {'Name': 'Bob Doe', 'Age': 40, 'Email': 'bobdoe@gmail.com', 'City': 'Seattle'}

user_info(**my_dict)