# this function directly modifies a list
def chop(elements):
    del elements[0]
    del elements[len(elements)-1]

# this function returns a new list created by slicing the original
def middle(elements):
    return elements[1:len(elements)-1]

elements = [1, 4, 6, 2, 8]
elements2 = [1, 4, 6, 2, 8]
chop(elements)
print(elements)

print(middle(elements2))
