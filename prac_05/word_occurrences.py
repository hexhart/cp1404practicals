"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
Word Occurrences program
"""

word_to_count = {}
text = input("Text: ")  # ask user for string input (random sentences)
words = text.split()  # each sentence is split into different words

# Count frequency of occurring words
for word in words:
    word_count = word_to_count.get(word, 0)  # non-existent word is added to dict, count = 1
    word_to_count[word] = word_count + 1  # word is an existing key in dict, count increment by 1

# Sorting the words (key) in ascending order
words = list(word_to_count.keys())
words.sort()

# get the maximum word length that exist in word_to_count
max_length = max((len(word) for word in words))

# print final output
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
