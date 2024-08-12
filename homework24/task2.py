# 2. Ի՞նչ տարբերություն(ներ) ունեն shallow copy և deep copy-ն։ Բերել օրինակներ, որտեղ հստակ նկարագրված կլինեն այդ տարբերությունները։

# Shallow copy-ն իրենից ներկայացնում է "մակերեսային" պատճենում։ Երբ նման պատճենում ենք կատարում nested օբյեկտները
# շարունակում են հղվել սկզբնական list-ի օբյեկտների վրա։ Այսինքն, եթե մենք փոխենք պատճենվածի nested-ի որևէ տարր,
# ապա սկզբնական list-ի տվյալ տարրը ևս կփոփոխվի։ Shallow copy կարող ենք իրականացնել [:] այսպես, կամ import անենք copy մոդուլը։

original_list = [[11, 22, 33], 44, 55]
shallow_copy_list = original_list[:]
shallow_copy_list[0][1] = 'word'
print(f'Original list: {original_list}')
print(f'Shallow copy: {shallow_copy_list}\n')

import copy

my_list = [12, 13, 14, [15, 16, 17]]
shallow_copy = copy.copy(my_list)
shallow_copy[3][2] = 'Python'
print(f'Original list: {my_list}')
print(f'Shallow copy: {shallow_copy}\n')


# Deep copy-ի դեպքում երբ պատճենում ենք սկզբնական list-ը, nested օբյեկտները ևս պատճենվում են։ Եթե փոփոխենք nested-ի որևէ
# տարր, ապա սկզբնական list-ում փոփոխություն տեղի չի ունենա, քանի որ nested օբյեկտների հասցեները կտարբերվեն։
# Deep copy կարող ենք իրականացնել import անելով copy մոդուլը։

original_lst = [22, [23, 24, 25], 26]
deep_copy = copy.deepcopy(original_lst)
deep_copy[1][1] = 'HELLO'
print(f'Original list: {original_lst}')
print(f'Deep copy: {deep_copy}')