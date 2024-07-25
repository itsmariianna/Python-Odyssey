# Write a function to log messages with varying levels of severity.
# Use *args to handle an arbitrary number of messages.
# Use **kwargs to handle keyword arguments for metadata (like timestamp, user, etc.).


def log_messages(level, *args, **kwargs):
    severity_levels = ['error', 'info', 'warning']

    if level not in severity_levels:
        print('\nPlease enter valid error')
        return

    for i in args:
        logging = f'{level.upper()} {i}'
        if kwargs:
            for key, value in kwargs.items():
                logging += f'\n{key} : {value}'
        print(logging)
    

log_messages('error', 'Something went wrong', user_name='Sam Smith', id=12345)

log_messages('debug', 'Something went wrong', user_name='Sam Smith', id=12345)

