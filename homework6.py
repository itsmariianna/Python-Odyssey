# June 11

# # Հայտարարել list,  որը բաղկացած է string-ներից: Տպել list-ում եղած ամենաերկար string-ը  և համապատասխան index-ը:
# ls = ['hello', 'longeststring', 'spam', 'ham']
# longest = ''
# indx = 0
# for i in range (len(ls)):
#     if len(ls[i]) > len(longest):
#         longest = ls[i]
#         indx = i
# print(f'The logest srting is "{longest}", and the index is {indx}')
    



# # Հայտարարել list,  որը բաղկացած է string-ներից: List-ում եղած բոլոր string-ների առաջին տառը դարձնել մեծատառ: Տպել յուրաքանչյուրի առաջին տառը:
# # Version 1
# ls = ['hello', 'apple', 'bye', 'banana']
# for i in range(len(ls)):
#     ls[i] = ls[i].capitalize()
# print(ls)
# for i in ls:
#     print(i[0])

# # Version 2
# ls = ['hello', 'apple', 'bye', 'banana']
# # for i in ls:
#     letter = i[0].upper()
#     print(letter)
    


# # Հայտարարել list և տպել list-ի էլեմենտները  հակառակ հերթականությամբ: List-ը կարող է պարունակել ցանկացած տիպի էլեմենտ:
# ls = [1, 4, 'hello', 7, 'okay']
# for i in range((len(ls)) -1, -1, -1):
#     print(ls[i])



# # Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։
# ls = [1, 4, 56, 9, 0, 2, 78]
# number = int(input("Enter number: "))
# if number in ls:
#     print("YES")
# else:
#     print("NO")



# # Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում:
# ls = ["apple", "oragne", "banana", "apple", "banana", "apple"]
# count = {}
# for i in ls:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)




# # Գրեք ծրագիր, որը ամբողջ թվային զանգվածի բոլոր զույգ էլեմենտները կտեղավորի նույն զանգվածի մեջ սկզբից, իսկ կենտերը՝ վերջից:
# ls = [11, 12, 43, 54, 75, 63, 77, 8, 99]
# even = []
# odd = []
# for i in ls:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even + odd)



# # Մուտքագրել քառակուսային մատրից և տպել էկրանին նրա տարրերը։
# rows = int(input("Enter the number of rows in matrix: "))
# columns = int(input("Enter the number of columns in matrix: "))

# matrix = []

# for i in range(rows):
#     row = []
#     for j in range(columns):
#         element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
#         row.append(element)
#     matrix.append(row)

# print(matrix)

    