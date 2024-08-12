# 10. Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա պետք է իրականացնել transpose։ Transpose կատարել նշանակում է մատրիցի տողերը փոխադրել սյուներով: 

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

lenght = len(matrix)

for i in range(lenght):
    for j in range(i + 1, lenght):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)