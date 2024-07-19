# 1. Write a recursive function to flatten a list that may contain nested lists.
def flatten_list(nested_list):
    flattened = []
    for i in nested_list:
        if isinstance(i, list):
            flattened.extend(flatten_list(i))
        else:
            flattened.append(i)
    return flattened
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
flattened_list = flatten_list(nested_list)
print(flattened_list)



# 2. Write a recursive function to calculate the sum of all elements in a list.
def sum_of_elements(my_list):
    if not my_list:
        return 0
    else:
        return my_list[0] + sum_of_elements(my_list[1:])

ls = [6, 7, 23, 4, 5]
print(sum_of_elements(ls))



# 3. Write a recursive function to check if a list is sorted in ascending order.
def ascending_order(my_list):
    if len(my_list) <= 1:
        return True
    if my_list[0] > my_list[1]:
        return False
    else:
        return ascending_order(my_list[1:])

ls_1 = [1, 2, 3, 4]
ls_2 = [3, 4, 1, 10]
print(ascending_order(ls_1))
print(ascending_order(ls_2))



# 4. Write a function that takes an integer as input and returns True if the number is prime, False otherwise.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    else:
        return True
check_number = int(input("Enter number: "))
result = is_prime(check_number)
print(f'{check_number} : {result}')



# 5. Write a function that takes three numbers as input and returns the maximum of the three.
def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
first = int(input("enter 1st number: "))
second = int(input("enter 2nd number: "))
third = int(input("enter 3rd number: "))
result = maximum_of_three(first, second, third)
print(f"The greatest number of the three is {result}")



# 6. Write a function that takes an integer n and returns a list of the first n Fibonacci numbers.
# Tarberak 1
def fib_numbers(n):
    ls = [0, 1]
    base_1 = 0
    base_2 = 1
    for i in range(0, n - 2):
        result = base_1 + base_2
        ls.append(result)
        base_1 = base_2
        base_2 = result
    return ls
number = int(input("Enter number: "))
print(fib_numbers(number))


# Tarberak 2
def fib_numbers_rec(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        ls = fib_numbers_rec(n - 1)
        ls.append(ls[-1] + ls[-2])
        return ls
number = int(input("Enter number: "))
print(fib_numbers_rec(number)) 



# 7. Write a function in Python that determines whether a given number is a power of 2. A number is considered a power of 2 if it can be expressed as 2^k, where k is a non-negative integer.
def power_of_two(n):
    if n <= 1:
        return False
    if n & (n - 1) == 0:
        return True
    else:
        return False

number = int(input("Enter number: "))
print(power_of_two(number))