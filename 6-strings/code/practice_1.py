# traversal through a string
fruit = 'banana'
index = 0
# while index is less than 6
while index < len(fruit):
    # get character at index 
    letter = fruit[index]
    # print the character
    print(letter)
    # increase index by 1
    index = index + 1

# another way to write a traversal
for char in fruit:
    print(char)