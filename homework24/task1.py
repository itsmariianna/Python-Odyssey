# 1. Ի՞նչ տարբերություն iterable և iterator տերմինների միջև։ Բերել օրինակներ, որտեղ համապատասխանաբար ներկայացված կլինեն այդ երկուսը։

# Iterable-ը օբյեկտ է, որի վրա կարող ենք իտերացիաներ կատարել։
# Այն ունի __iter__() մեթոդ:
# Iterable օբյեկտ են հանդիսանում string, dictionary, list, tuple:

ls = [1, 2, 3, 4]
for i in ls:
    print(i)

# Iterator-ի միջոցով կարող ենք iterable օբյեկտի ամեն էլէմենտի վրայով անցնել ցիկլերի միջոցով։
# Այն ունի __iter__() և __next__() մեթոդները և պետք է դրանք իմպլեմետացնի։
# Ունի կանգառի պայման, որից հետո տեղի է ունենում StopIteration։ 
# iter ֆունկցիան ենք կիրառելով Iterable-ի վրա կստանանք Iterator։

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print("Start")
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        print("Iteration ended")
        break
