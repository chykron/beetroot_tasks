"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values.
"""

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

unique_words = dict()

for word in words:
    if word in unique_words:
        unique_words[word] += 1
    else:
        unique_words[word] = 1
print(unique_words)
