# Իրականացնել ֆունկցիա, որն ընդունում է բառերի ցուցակ և վերադարձնում է համապատասխան բառերի երկարությունները ներկայացնող ամբողջ թվերի ցուցակ: Օգտագործել ցուցակի ըմբռնումը(list comprehension), ինչպես նաև տրամադրել այլընտրանքային լուծում ՝ օգտագործելով map ֆունկցիա:

def my_func(ls: list) -> list:
    lenght_list = [len(word) for word in ls]
    return lenght_list

my_list_1 = ['apple', 'stop', 'python', 'hello', 'okay']
print(my_func(my_list_1))


# Այլընտրանք

my_list_2 = ['hello', 'bye', 'python', 'ok']
result = map(lambda x: len(x), my_list_2)
print(list(result))