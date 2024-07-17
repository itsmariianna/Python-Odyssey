# 1. Write a recursive function to print numbers from 1 to 5.
def numbers(x):
    if x > 5:
        return
    else:
        print(x)
        return numbers(x + 1)
numbers(1)



# 2. Write a recursive function to print numbers from 5 to 1.
def numbers(x):
    if x < 1:
        return
    else:
        print(x)
        return numbers(x - 1)
numbers(5)



# 3. Write a recursive function to calculate the factorial of a given number.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)    

number = int(input("Enter number: "))
result = factorial(number)
print(f'{number}! = {result}')



# 4. Write a recursive function to find the sum of the first N natural numbers.
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)

number = int(input("Enter: "))
res = sum_of_numbers(number)
print(res)



# 5. Write a recursive function to print all elements of a list.
def all_elements(my_list):
    if not my_list:
        return
    print(my_list[0])
    all_elements(my_list[1:])

ls = [6, 'spam', 'ham', 10]
all_elements(ls)



# 6. Write a recursive function to find the length of a list.
def lenght_list(ls):
    if not ls:
        return 0
    else:
        lenght = 1 + lenght_list(ls[1:])
        return lenght
my_list = [1, 2, 3, 9]
result = lenght_list(my_list)
print(result)



# 7. Write a recursive function to reverse a given string.
def reverse_string(my_string):
    if len(my_string) <= 1:
        return my_string
    else:
        return my_string[-1] + reverse_string(my_string[:-1])
str = input("Enter word: ")
print(reverse_string(str))




# 8. Write a recursive function to generate the Nth Fibonacci number.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
        return fib
number = int(input("Enter number: "))
result = fibonacci(number)
print(result)




# 9. Write a recursive function to print each character of a string on a new line.
def new_line(my_string):
    if not my_string:
        return
    else:
        print(my_string[0])
        new_line(my_string[1:])
str = input("Enter word: ")
new_line(str)



# 10. Write a recursive function to check if a given string is a palindrome.
def palindrome_sting(my_string):
    if len(my_string) <= 1:
        return True
    if my_string[0] != my_string[-1]:
        return False
    else:
        return palindrome_sting(my_string[1:-1])

str = input("Enter word: ")
print(palindrome_sting(str))




# 11. Write a recursive function to find the sum of the digits of a given number.
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        sum = (n % 10) + sum_of_digits(n // 10)
        return sum
number = int(input("Enter number: "))
result = sum_of_digits(number)
print(result)
