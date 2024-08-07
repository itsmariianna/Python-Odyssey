# Use the filter function with a lambda to filter out all even numbers from a list.
even = lambda x : x % 2 == 0

ls = [1, 2, 3, 4, 5, 6]

print(list(filter(even, ls)))