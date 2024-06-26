#June 25

# # 1. Write a program that searches through the string “find the letter z” and prints the index of the first occurrence of ‘z’. If ‘z’ is not found, print “Character not found”.
# string = input("Enter a word to check if there is the letter Z: ").lower()
# for i in range(len(string)):
#     if string[i] == 'z':
#         print(f'Z found at index {i}')
#         break
# else:
#     print("Character not found")



# # 2. Given the string “capitalize”, transform the first character to uppercase to make it “Capitalize” (use ASCII table). Hint (the difference between the ASCII values of a lowercase letter and its corresponding uppercase letter is 32. Specifically, to convert a lowercase letter to uppercase, you subtract 32 from its ASCII value.)
# string = "capitalize"
# cap = chr(ord(string[0])-32)
# print(cap+string[1:])



# # 3. Convert the string “hello, world! are you ready?” into title case, where each word starts with an uppercase letter, resulting in “Hello, World! Are You Ready?“. (use ASCII table)
# string = "hello, world! are you ready?".split()
# for i in string:
#     if ord('a') < ord(i[0]) < ord('z'):
#         print(i[0].upper()+i[1:], end = ' ')




# # 4. Create a program that reverses the string “reverse me” and prints “em esrever”.
# string = 'reverse me'
# for i in range(len(string) -1, -1, -1):
#     print(string[i], end = '')



# # 5. Write a program that checks if the string “radar” is a palindrome (reads the same forward and backward) and print “Yes” if it is, or “No” if it is not.
# word = 'radar'
# reversed = word[::-1]

# if word == reversed:
#     print("Yes")
# else:
#     print("No")



# # 6. Given two strings, “hello” and “world”, write a program to concatenate them with a space in between, resulting in “hello world”.
# string_1 = 'hello'
# string_2 = 'world'
# joined_string = ''
# for i in string_1:
#     joined_string += i

# joined_string += ' '

# for i in string_2:
#     joined_string += i

# print(joined_string) 



# # 7. Write a program that replaces every occurrence of the letter ‘a’ with ‘x’ in the string “banana” and prints “bxnxnx”.
# word = 'banana'
# new_word = ''

# for i in word:
#     if i == 'a':
#         i = 'x'
#     new_word += i

# print(new_word)