# 9. Python-ում ցիկլային գործողությունների հետ հնարավոր է կիրառել else պայմանական հայտարարությունը։ Բերել օրինակ որտեղ ներկայացված կլինի այդ հայտարարության օգտագործումը և սահմանել, թե ինչու է ցանկալի խուսափել նման հայտարարություններից։

# else բլոկը կատարվում է միայն այն ժամանակ, երբ ցիկլից նորմալ դուրս ենք գալիս, առանց break-ի հանդիպելու։
# Այսինքն, եթե ինչ-որ բան կա else բլոկի մեջ, ապա այն կարող է բաց թողնվել այն ժամանակ, եթե loop-ի մեջ լինի break ու դրա
# միջոցով դուրս կգանք ցիկլից։

def find_prime(numbers):
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(f"{number} is a prime")

find_prime([14, 15, 16, 17, 18, 19])


# Այս նույնը կարող ենք գրել առանց else-ի, օգտագործելով flag
print()

def is_prime(my_list):
    for i in my_list:
        flag = True
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                print(f'{i} is prime')

is_prime(([5, 6, 7, 8, 9]))


