# Write a function make_logger(level) that returns a function which logs messages with the specified log level.
def make_logger(level):
    def logger(message):
        return f'{level} : {message}'
    return logger

result = make_logger("ERROR")
print(result("This is an error message"))