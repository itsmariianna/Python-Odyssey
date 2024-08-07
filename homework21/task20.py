# Create a dictionary with functions for basic file operations (e.g., read, write, append, delete). Write a function file_manager(file_name, operation, content=None) that uses this dictionary to perform the requested file operation.

import os

file_operations = {
    'read': lambda file_name: open(file_name, 'r').read() if os.path.exists(file_name) else 'File not found',
    'write': lambda file_name, content: (open(file_name, 'w').write(content), 'File written successfully')[1],
    'append': lambda file_name, content: (open(file_name, 'a').write(content), 'Content appended successfully')[1],
    'delete': lambda file_name: (os.remove(file_name), 'File deleted successfully')[1] if os.path.exists(file_name) else 'File not found'
}

def file_manager(file_name, operation, content=None):
    if operation in file_operations:
        try:
            if content is None:
                return file_operations[operation](file_name)
            else:
                return file_operations[operation](file_name, content)
        except Exception as e:
            return f'Error: {str(e)}'
    else:
        return 'Operation not supported'

print(file_manager('example.txt', 'write', 'Hello, world!'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'append', ' Appended text.'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'delete'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'ankap'))
