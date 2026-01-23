# task 6: Write a program to count how many lines, words, and characters are in a given text file.

# from math import sum

def count_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"the number of lines are: {len(lines)}")

        word_count = sum([len(line.split()) for line in lines])
        print(f"the number of words are: {word_count}")

        char_count = sum([len(char) for line in lines for char in line if not char.isspace()])
        print(f"the number of chars are: {char_count}")

count_content('test.txt')