# Store functions for text processing (e.g., word count, character count, find word, replace word) in a dictionary. Write a function process_text(text, operation, **kwargs) that uses this dictionary to perform the requested text processing operation.

text_processing = {'word count' : lambda text: len(text.split()),
                   'character count' : lambda word : len(word),
                   'find word' : lambda text, word: text.count(word),
                   'replace word' : lambda text, old, new : text.replace(old, new)}


def process_text(text, operation, **kwargs):
    if operation in text_processing:
        func = text_processing[operation]
        if operation == 'find word':
            if 'word' in kwargs:
                return func(text, kwargs['word'])
            else:
                return 'Missing word'

        elif operation == 'replace word':
            if 'old' in kwargs and 'new' in kwargs:
                return func(text, kwargs['old'], kwargs['new'])
            else:
                return 'Something is missing'
            
        else:
            return func(text)
    else:
        return 'There is no such operation'
    

print(process_text('Hello world!', 'word count'))
print(process_text('Hello world!', 'character count'))
print(process_text('Hello world!', 'find word', word = 'Hello'))
print(process_text('Hello world!', 'replace word', old = 'Hello', new = 'Bye'))
print(process_text('Hello world!', 'lenght'))