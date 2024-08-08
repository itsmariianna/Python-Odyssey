# Իրականացնել make_multiplier closure, որն ընդունում է մեկ n արգումենտ ր վերադարձնում է մեկ այլ ֆունկցիա։ Այս վերադարձված ֆունկցիան պետք է ընդունի մեկ X արգումենտ և վերադարձնի n և X արտադրյալը։ Իրականացնել ծրագիրը օգտագործելով միայն Lambda ֆունկցիաներ։

make_multiplier = lambda n: lambda X: n * X
multiplier_of_3 = make_multiplier(3)
print(multiplier_of_3(10))