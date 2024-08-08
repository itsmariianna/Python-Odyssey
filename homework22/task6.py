# Ի՞նչ տարբերություն iterable և iterator տերմինների միջև։ Բերել օրինակներ, որտեղ համապատասխանաբար ներկայացված կլինեն այդ երկուսը։


# Iterable-ը ունի __iter__() մեթոդը։ Հանդիսանում է օբյեկտ, որի վրա կարող ենք իտերացիաներ կատարել loop-երի միջոցով։ Օրինակներ են հանդիսանում list,
# tuple, string, dictionary, set: Օրինակ՝

ls = [1, 2, 3, 4]
for i in ls:
    print(i)


# Iterator-ը պետք է իմպլեմետացնի __iter__() և __next__() մեթոդները։ Այն օգտագործվում է հաջորդականության յուրաքանչյուր տարրի վրայով անցնելու համար։
# Որպեսզի Iterable-ից ստանանք Iterator օգտագործում ենք iter ֆունկցիան։ Օրինակ՝

numbers = [11, 22, 33, 44]
iterator = iter(numbers)
while True:
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break
