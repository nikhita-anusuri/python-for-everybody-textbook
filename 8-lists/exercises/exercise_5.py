file_name = input("Enter a file name: ")
fhand = open(file_name)
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])
print(f'There were {count} lines in the file with From as the first word')



