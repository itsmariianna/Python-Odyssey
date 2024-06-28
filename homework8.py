# June 28

# # 1. Write a program that inserts a value at a specified index in a list without using the built-in insert() method. For example, insert the value 3 at index 1 in the list [1, 2, 4, 5] to make it [1, 3, 2, 4, 5].
# ls = [1, 2, 4, 5]
# indx = int(input("Enter index: "))
# value = int(input("Enter value: "))
# ls[indx:indx] = [value]
# print(ls)



# # 2. Write a program that removes the first occurrence of a specified element from a list without using the remove() method. If the element does not exist, print a message. Example: Remove 2 from [1, 2, 3, 2, 4] resulting in [1, 3, 2, 4].
# ls = [1, 2, 3, 2, 4]
# element = int(input("Enter number: "))
# for i in range(len(ls)):
#     if ls[i] == element:
#         del ls[i]
#         print(f'New list: {ls}')
#         break
# else:
#     print("There is no such element")



# # 3. Write a program that removes and returns the last element of a list without using the pop() method. If the list is empty, return a message indicating it is empty. Example usage on [1, 2, 3] should return 3 and the list becomes [1, 2].
# ls = [1, 2, 4, 5]
# if len(ls) == 0:
#     print("List is empty")
# else:
#     last_element = ls[-1]
#     ls = ls[:-1]
#     print(f"Removed number: {last_element}\nNew list: {ls}")



# # 4. Develop a program that clears all elements from a list without using the clear() method. After running the function on [1, 2, 3], the list should be empty.
# ls = [1, 2, 3, 6, 7, 9]
# for i in range(len(ls)):
#     del ls[0]
# print(ls)



# # 5. Use list comprehension to generate a list of squares for all integers from 1 to 10. The resulting list should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# ls = [x ** 2 for x in range(1, 11)]
# print(ls)



# # 6. Write a single line of Python using list comprehension to filter and create a list of even numbers from an existing list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], resulting in [2, 4, 6, 8, 10].
# all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ls = [x for x in all_numbers if x % 2 == 0]
# print(ls)