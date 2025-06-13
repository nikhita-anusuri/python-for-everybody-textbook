word_dictionary = {}
words_file = open('words.txt')
for line in words_file:
    words = line.split()
    for word in words:
        word_dictionary[word] = True
print(word_dictionary)