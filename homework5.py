# # Implement a Python program that asks the user to enter a password. If the password matches a predefined secret password, display a success message. Otherwise, display an error message using an if/else ternary expression.
# # Version 1
# predefined_password = 345621
# user_password = int(input("Enter password: "))
# if predefined_password == user_password:
#     print("SUCCESS")
# else:
#     print("ERROR")

# # Using random
# import random
# predefined_password = random.randint(100000, 999999)
# user_password = int(input("Enter password: "))
# if predefined_password == user_password:
#     print("SUCCESS")
# else:
#     print("ERROR")



# # Write a Python program that prints all the prime numbers between 1 and 100 using a for loop and the break keyword.
# for num in range (1, 101):
#     if num > 1:
#         for j in range (2, num):
#             if num % j == 0:
#                 break
#         else:
#             print(num)
