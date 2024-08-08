# Ի՞նչ տարբերություն(ներ) ունեն shallow copy և deep copy-ն։ Բերել օրինակներ, որտեղ հստակ նկարագրված կլինեն այդ տարբերությունները։


# Shallow copy - ստեղծում է նոր օբյեկտ, բայց չի ստեղծում nested օբյեկտների պատճենները: Նախնական և նոր ստեղծված օբյեկտները շարունակում են հղվել
# միևնույն  օնյեկտների վրա։ Shallow copy կարող ենք իրականացնել օգտագործելով [:] կամ copy մոդուլը import անելով։ Օրինակ՝
import copy

original_list = [[1, 2, 3], 4, 5]
shallow_copy_list = original_list[:]
shallow_copy_list[0][1] = 'hello'
print(f'Original list: {original_list}')        # Output [[1, 'hello', 3], 4, 5]
print(f'Shallow copy: {shallow_copy_list}')     # Output [[1, 'hello', 3], 4, 5]

# Օգտագործենք copy module

original_list_import = [[1, 2, 3], 4, 5]
shallow_copy_list_import = copy.copy(original_list_import)
shallow_copy_list_import[0][1] = 'hello'
print(f'Original list (using import module): {original_list_import}')
print(f'Shallow copy (using import module): {shallow_copy_list_import}')



# Deep copy - ստեղծում է նոր օբյեկտ, որտեղ nested օբյեկտները չեն հղվում են սկզբնական օբյեկտի տարրերի վրա։ Փոփոխելով նոր օբյեկտի nested-ի տարերը
# չենք փոփոխի սկզբնական օբյեկտի nested-ի տարրերը։ Deep copy կարող ենք իրականացնել օգտագործելով copy մոդուլը import անելով։ Օրինակ՝

original_list_deep = [1, 2, 3, [5, 6, 7]]
deepcopy_list = copy.deepcopy(original_list_deep)
deepcopy_list[3][1] = 'hello'
print(f'Original list: {original_list_deep}')    # Output [1, 2, 3, [5, 6, 7]]
print(f'Deep copy: {deepcopy_list}')             # Output [1, 2, 3, [5, 'hello', 7]]