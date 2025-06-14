import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    # this removes punctuation from the line
    line = line.translate(str.maketrans('', '', string.punctuation))
    # makes line lowercase
    line = line.lower()
    # turns line into a list of elements
    # elements are decided by splitting at spaces
    words = line.split()
    # for loop going through each element in list of words
    for word in words:
        # if statement checks if word is not in the dictionary named counts
        if word not in counts:
            # add word as a key for counts dictionary
            counts[word] = 1
        else:
            # if it already exists as a key then it adds 1 to the value
            counts[word] += 1

# sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for count, word in lst[:10]:
    print(word, count)