fname = input("Enter a file name: ")
mail_file = open(fname)
days = {}
for line in mail_file:
    words = line.split() # lines become lists
    if len(words) < 3 or words[0] != 'From':
        continue
    day = words[2]
    # the get method takes in a key and a default value
    # if the key already exists in the dictionary, the corresponding
    # value will be returned
    # else the default value will be returned
    days[day] = days.get(day, 0) + 1

print(days)

