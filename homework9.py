# June 30

# # 1. Գրել ծրագիր, որը կստուգի երկու նույն չափի զանգվածները նույնն են, թե ոչ։ Այսինքն արդյոք բոլոր համապատասխանող ինդեքսներով արժեքները համընկնում են, թե ոչ։
# # Version 1
# ls_1 = [1, 3, 4, 5, 6]
# ls_2 = [1, 3, 4, 5, 9]
# flag = True
# for i in range(len(ls_1)):
#     if ls_1[i] != ls_2[i]:
#         flag = False
#         print("Not equal")
#         break
# if flag:
#     print("Equal")


# # Version 2
# ls_1 = [1, 3, 4, 5, 6]
# ls_2 = [1, 3, 4, 5, 6]
# lenght = len(ls_1) - 1
# for i in range(lenght):
#     if ls_1[lenght] == ls_2[lenght]:
#         print("Equal lists")
#         break
#     else:
#         print("Not equal lists")
#         break



# # 2. Գրել ծրագիր, որն օգտագործողին թույլ կտա մուտքագրել ամբողջ թվային զանգվածի էլեմենտների արժեքները և կգտնի զանգվածի ամենամեծ և ամենափոքր տարրերի ինդեքսների տարբերությունը:
# number = int(input("Enter number: "))
# ls = []
# for i in range(number):
#     element = int(input("Enter: "))
#     ls.append(element)
# print(ls)

# small_index = 0
# large_index = 0

# for i in range(1, number):
#     if ls[i] < ls[small_index]:
#         small_index = i

# for j in range(1, number):
#     if ls[j] > ls[large_index]:
#         small_index = j

# difference = abs(large_index - small_index)
# print(f"The smallest index is: {small_index}\nThe largest index is: {large_index}\nDifference is: {difference}")



# # 3. Մուտքագրել քառակուսային մատրից և տպել էկրանին նրա տարրերը։
# matrix = []
# size = int(input("Enter size: "))
# for i in range(size):
#     row = []
#     for j in range(size):
#         element = int(input(f'Enter element for {i}{j} position: '))
#         row.append(element)
#     matrix.append(row)
# print(matrix)



# # 4. Իրականացնել ծրագիր, որը քառակուսային մատրիցի գլխավոր և օժանդակ անկյունագծի էլեմենտների արժեքները տեղերով կփոխի։
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for i in range(len(matrix)):
#     matrix[i][i], matrix[i][len(matrix) - i - 1] = matrix[i][len(matrix) - i - 1], matrix[i][i]

# print(matrix)


# # 5. Իրականացնել Ծրագիր, որը հաշվում է քառակուսային մատրիցի գլխավոր անկյունագծի տարրերի գումարը։
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# sum = 0
# for i in range(len(matrix)):
#     sum += matrix[i][i]
# print(sum)




# # 6. Իրականացնել ծրագիր, որը հաշվում է քառակուսային մատրիցի օժանդակ անկյունագծի տարրերի գումարը։
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# sum = 0
# for i in range(len(matrix)):
#     sum += matrix[i][len(matrix) - 1 - i]
# print(sum)




# # 7. Գրել ծրագիր, որը կգտնի NxM (N քանակությամբ տող և M քանակությամբ սյուն) չափանի մատրիցի մեծագույն արժեքը և կտպի էկրանին
# matrix = []
# size_column = int(input("Enter size of columns: "))
# size_row = int(input("Enter size of rows: "))
# for i in range(size_row):
#     row = []
#     for j in range(size_column):
#         element = int(input(f'Enter element for {i}{j} position: '))
#         row.append(element)
#     matrix.append(row)

# print(matrix)
    
# max_element = matrix[0][0]
# for row in matrix:
#     for element in row:
#         if element > max_element:
#             max_element = element
# print(f'The maximum value is {max_element}')

