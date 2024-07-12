# Գրել ֆունկցիա, որը ստանում է n բնական թիվ և տպում է n-ից 0 թվերը։
def my_func(n):
    ls = []
    for i in range(n, -1, -1):
        ls.append(i)
    return ls

number = int(input("Enter number: "))
print(my_func(number))



# Գրել ֆունկցիա, որը ստանում է n բնական թիվ և տպում է 0-ից n թվերը։
def my_func(n):
    ls = []
    for i in range(0, n + 1):
        ls.append(i)
    return ls

number = int(input("Enter number: "))
print(my_func(number))


# Գրել ֆունկցիա, որը ստանում է list և տպում է list-ի էլեմենտները էկրանին։
def list_elements(ls: list):
    for i in ls:
        print(i)

my_list = [1, 3, 'apple', (3, 5), 9]
list_elements(my_list)



# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը: (123 -> 1 + 2 + 3)
def sum_of_integers(n):
    count = 0
    while n > 0:
        digit = n % 10
        count += digit
        n = n // 10
    return count

number = int(input("Enter number: "))
print(f'Sum of numbers: {sum_of_integers(number)}')




# Իրականացնել ֆունկցիա, որը ստանում է տող և վերադարձնում տողում առաջին հանդիպած մեծատառը։
def first_uppercase(str):
    for i in str:
        if i.isupper():
            return i
        return "There is no uppercase"

my_str = input("Enter string: ")
print(first_uppercase(my_str))




# Իրականացնել ֆունկցիա, որը ստանում է list և վերադարձնում list-ի ամենափոքր (ամենամեծ) էլեմենտը։
def min_and_max(ls):

    min_element = ls[0]
    max_element = ls[0]

    for i in range(len(ls)):
        if ls[i] > max_element:
            max_element = ls[i]
        if ls[i] < min_element:
            min_element = ls[i]
    return f'Maximum element: {max_element}\nMinimum element: {min_element}' 

my_ls = [4, 5, 2, 10, 9, 3]
print(min_and_max(my_ls))