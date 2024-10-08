# 8. Ի՞նչ տարբերություններ կան list և tuple ներկառուցված տիպերի միջև։ Հիմնավորել պատասխանը։

# List-ը հանդիսանում է հաջորդականություն, որը mutable է, այսինքն կարող ենք տեղում փոփոխություններ կատարել։ Դրա 
# պատճառով է, որ ավելի դանդաղ է, քան tuple-ը
# Կարող է պարունակել ցանկացած տիպի օբյեկտ։

lst_1 = [1, 2, 3, 4]
lst_2 = [1, 'hello', {'name': 'Ann', 'age': 12}, (1, 2, 3)]

# Ի տարբերություն list-ի, tuple-ը immutable է, այինքն տեղում փոփոխություն չենք կարող կաատրել։ Սրա պատճառով կարող են
# հանդիսանալ dictionary-ի key-եր։ Կօգտագործենք այն ժամանակ, երբ չենք ցանկանում այլ user կարողանա փոփոխել մեր տվյալները։
# Ավելի քիչ մեթոդներ են հասանելի, ի տարբերություն list-ի։

tp_1 = ({"key1": "value1", "key2": "value2"}, 42, "hello")
tp_2 = ([1, 2, 3], 4, 'hello')
