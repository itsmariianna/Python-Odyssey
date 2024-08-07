# Implement a function make_config(key, value) that returns a function which, when called, returns a dictionary with the given key-value pair.

def make_config(key, value):
    def inner():
        return {key:value}
    return inner

result = make_config('Bob', 34)
print(result())