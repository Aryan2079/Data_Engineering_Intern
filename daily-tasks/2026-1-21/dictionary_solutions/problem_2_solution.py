# Dictionary problem 2: Write a function that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the frequencies of those words.
# eg:
# input: 'the quick brown fox jumps over the lazy dog'
# output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

def foo(s):
    output = {}
    words = s.split(' ')

    for word in words:
        freq = output.setdefault(word, 0)
        output[word] = freq+1
    print(output)

foo('the quick brown fox jumps over the lazy dog')