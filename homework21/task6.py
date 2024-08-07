# Use the map function with a lambda to square all elements in a list.

square = lambda x : x ** 2

ls = [1, 2, 3, 4, 5]

print(list(map(square, ls)))