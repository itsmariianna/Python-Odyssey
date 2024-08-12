# Write a function that reads a text file and counts the number of lines, words, and characters in the file. Then, write these statistics to a new file.
def count_file(file, statistics):
    lines = 0
    words = 0
    characters = 0

    with open(file, 'r') as file:
        for i in file:
            lines += 1
            words += len(i)
            characters += len(i.split())

    data = f'Lines: {lines}\nWords: {words}\nCharacters: {characters}'

    with open(statistics, 'w') as statistics:
        statistics.write(data)

    return f"You can see statistics in your file"

my_file = 'file.txt'
my_statistics = 'statistics.txt'

print(count_file(my_file, my_statistics))