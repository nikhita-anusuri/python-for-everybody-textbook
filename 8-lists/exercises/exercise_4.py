unique_words = []
file_name = input("Enter file: ")
book = open(file_name)
for line in book:
    words = line.split()
    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)

unique_words.sort()
print(unique_words)