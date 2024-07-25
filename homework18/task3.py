# Create a function to print a user profile.
# Use keyword-only arguments for age and city.
# Use positional arguments for first name and last name. (print_user_profile("John", "Doe", age=30, city="New York")
# Return the result of the operation.


def user_profile(name, surname, *, age, city):
    return f'User profile\nName: {name} {surname}\nAge: {age}\nCity: {city}'

result = user_profile("John", "Doe", age=30, city="New York")
print(result)
