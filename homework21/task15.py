# Store functions for string manipulations (such as uppercase, lowercase, title case, and reversing a string) in a dictionary. Write a function manipulate_string(s, operation) that takes a string and an operation name, and uses the dictionary to perform the requested string manipulation.
string_manipulations = {'uppercase' : lambda word: word.upper(),
                        'lowercase' : lambda word: word.lower(),
                        'titlecase' : lambda text: text.title(),
                        'reverse' : lambda word: word[::-1]}


def manipulate_string(s, operation):
    if operation in string_manipulations:
        return string_manipulations[operation](s)
    else:
        return 'There is no such operation'
    
print(manipulate_string('hello', 'uppercase'))
print(manipulate_string('HELLO', 'lowercase'))
print(manipulate_string('hello world', 'titlecase'))
print(manipulate_string('hello', 'reverse'))
print(manipulate_string('hello', 'lenght'))
