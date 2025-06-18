fname = input("Enter a file name: ")
fhand = open(fname)

letter_counts = {}
for line in fhand:
    line = line.lower()
    for char in line:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

tuples_list = []
for key in letter_counts:
    tuples_list.append((letter_counts[key], key))
tuples_list.sort(reverse=True)    

for tuple in tuples_list:
    print(tuple[1], tuple[0])
