# Create a Python script that generates a text file named append_mode.txt. Open the file in append mode and write some text into it. If the file already exists, the new text should be added at the end of the file.
with open('append_mode.txt', 'a') as file:
    file.write("This is some text that will be appended.\n")
    file.write("Appending another line here.\n")
print("Text appended successfully.")



# Create a Python script that generates a text file named exclusive_mode.txt. Open the file in exclusive creation mode ('x') and write some text into it. If the file already exists, the script should raise a FileExistsError.
try:
    with open('exclusive_mode.txt', 'x') as file:
        file.write("This file was created using exclusive mode.\n")
        file.write("It will not overwrite any existing file.\n")
    print("File created successfully.")

except FileExistsError:
    print("Error: The file 'exclusive_mode.txt' already exists.")



# Create a Python script that generates a text file named specific_position.txt. Open the file in read and write mode ('r+'). Write some text at a specific position in the file. If the file does not exist, create it first with some initial text.
filename = 'specific_position.txt'
try:
    with open(filename, 'x') as file:
        file.write("This is the initial text.\n")
except FileExistsError:
    pass

with open(filename, 'r+') as file:
    file.seek(25)
    file.write("Inserted text here. ")

print("Text written at the specified position successfully.")



# Create a Python script that processes a given text file to find and count the occurrences of a specific word. For this task, you will use a sample text file and count how many times the words “example”, “all”, “word”, “up”, “did”, “him” appear.
filename = 'specific_word.txt'
words_to_count = ["example", "all", "word", "up", "did", "him"]
word_count = {word: 0 for word in words_to_count}

try:
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1

    for word, count in word_count.items():
        print(f"'{word}': {count} occurrences")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
