# you have a list of words and want to sort them from longest to shortest
txt = 'but soft what light in yondeer window breaks'
words = txt.split()
t = list()
for word in words:
    # creating a tuple inside list named t each iteration
    t.append((len(word), word))

t.sort(reverse=True)

# create new list named res
res = list()
for length, word in t:
    # each time it loops it takes each word from the sorted tuple
    # and puts them in the list
    res.append(word)
# this results in a list with the words from the original string
# ordered by length
print(res)
