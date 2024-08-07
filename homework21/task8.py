# Implement a function make_greeting(greeting) that takes a greeting string and returns a function that takes a name and prints the greeting followed by the name.
def make_greeting(greeting):
    def user_name(name):
        return f'{greeting}, {name}'
    return user_name

result = make_greeting("Hello")
print(result("Bob"))