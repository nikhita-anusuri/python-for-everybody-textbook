list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = []
for x in list_of_ints_in_strings:
    list_of_ints.append(int(x))
print(list_of_ints)

list_of_ints_in_strings2 = ['42', '65', '12']
list_of_ints2 = [ int(x) for x in list_of_ints_in_strings2 ]
print(list_of_ints2)
