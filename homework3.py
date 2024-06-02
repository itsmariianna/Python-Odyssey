# #1. Գրել ծրագիր, որը կտպի 1-ից 10 թվերի քառակուսիները:
# for i in range (1, 11):
#     result = i ** 2
#     print(result)

# #2. Գրել ծրագիր, որը տրված թվերի ցուցակից կընտրի միայն դրական թվերը և կտպի դրանք:
# numbers = [-5, 3, -1, 101, -33, 44, 0, 7]
# even = []
# for i in numbers:
#     if i > 0:
#         even.append(i)
#     else:
#         continue
# print(even)


# #3. Գրել ծրագիր, որը կտպի 1-ից 20 միջակայքում գտնվող այն թիվերը, որոնք բազմապատիկ են 3-ի:
# for i in range (1, 21):
#     if i % 3 == 0:
#         print(i)


# #4. Գրել ծրագիր, որը կտպի տրված բառի յուրաքանչյուր տառը և իր ինդեքսը
# word = "python"
# word_ls = list(word)
# for i in word_ls:
#     index_word = word_ls.index(i)
#     print(f'{i} : {index_word}')


# #5. Պարզ հաշվիչի ստեղծում.
# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))
# operation = input("Enter arithmetic operations (+, -, *, /): ")
# if operation == "+":
#     add = num_1 + num_2
#     print(f'The addition operation combines two numbers to find their sum: {add}')
# if operation == "-":
#     diff = num_1 - num_2
#     print(f'The subtraction operation finds the difference between two numbers: {diff}')
# if operation == "*":
#     mul = num_1 * num_2
#     print(f'The multiplication operation finds the product of two numbers: {mul}')
# if operation == "/":
#     if num_2 == 0:
#         print("You can't divide by zero")
#     elif num_2 > 0:
#         div = num_1 / num_2
#         print(f'The division operation divides one number by another to find the quotient.: {div}')
# else:
#     print("Please enter arithmetic operation which is mentioned above")

