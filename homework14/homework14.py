# Create a Python script that generates a text file named append_mode.txt. Open the file in append mode and write some text into it. If the file already exists, the new text should be added at the end of the file.
with open('append_mode.txt', 'a') as file:
    file.write('New line for your file\n')
print('File created and text written')




# Create a Python script that generates a text file named exclusive_mode.txt. Open the file in exclusive creation mode ('x') and write some text into it. If the file already exists, the script should raise a FileExistsError.
try:
    with open('exclusive_mode.txt', 'x') as file:
        file.write('This is a new line of text')
    print('File created and text written')
except FileExistsError:
    print('The file already exists')

 


# Create a Python script that generates a text file named specific_position.txt. Open the file in read and write mode ('r+'). Write some text at a specific position in the file. If the file does not exist, create it first with some initial text.
try:
    with open('specific_position.txt', 'r+') as file:
        file.seek(8)
        file.write('INSERTED')
        print('Text has been written')

except FileNotFoundError:
    with open('specific_position.txt', 'w') as file:
        file.write('Initial text in the file.')
    
    with open('specific_position.txt', 'r+') as file:
        file.seek(8)
        file.write('INSERTED TEXT')
        print('File created and text written')



# Create a Python script that processes a given text file to find and count the occurrences of a specific word. For this task, you will use a sample text file and count how many times the words “example”, “all”, “word”, “up”, “did”, “him” appear.
words_list = ['example', 'all', 'word', 'up', 'did', 'him']
word_count = {word: 0 for word in words_list}
try:
    with open('example.txt', 'r') as file:
        text = file.read().lower()
        
        for i in words_list:
            word_count[i] = text.count(i)

    for word, count in word_count.items():
        print(f"{word} : {count}")

except FileNotFoundError:
    print("The file doesn't exist.")
