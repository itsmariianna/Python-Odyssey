# Create a dictionary-based calculator where each arithmetic operation (addition, subtraction, multiplication, division) is a function stored in a dictionary. Write a function calculate(operand1, operand2, operator) that uses this dictionary to perform the requested operation.

operations = {'+' : lambda x, y : x + y,
              '-' : lambda x, y : x - y,
              '*' : lambda x, y : x * y,
              '/' : lambda x, y : x / y if y != 0 else "You can't divide by zero"}

def calculate(operand1, operand2, operator):
    if operator in operations:
        return operations[operator](operand1, operand2)
    else:
        return "There is no such operation"
    
print(calculate(18, 6, '+'))
print(calculate(10, 9, '-'))
print(calculate(78, 7, '*'))
print(calculate(2, 5, '/'))
print(calculate(2, 0, '/'))
print(calculate(2, 9, '//'))