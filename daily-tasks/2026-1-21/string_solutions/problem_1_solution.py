# String problem 1: Write a function that takes a string as input and returns a list of all the words in the string that are longer than 5 characters. While returning the words, alternately capitalize the letters.
# Example:

# -- basic string operation
# input: 'The quick brown fox jumps over the lazy dog'
# Output: ['quick', 'brown', 'jumps']

def foo(sentence):
    output = []
    words = sentence.split(' ')
    for item in words:
        if len(item) >= 5:
            output.append(item)

    print(output)

foo('The quick brown fox jumps over the lazy dog')