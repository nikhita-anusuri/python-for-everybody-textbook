t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t)

print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

t[1:3] = ['x', 'y']
print(t)

# adds element to end of list
t.append('g')
print(t)

# appends each element of the argument list to the original list
x = ['h', 'i']
t.extend(x)
print(t)

# sorts elements in array
t.sort()
print(t)

lst = [1, 2, 3, 4]
lst.append([[3, 4, 5]])
print(lst)
#[1, 2, 3, 4, [[3, 4, 5]]]

lst.extend([[3, 4, 5], 5, 6, [7, 8]])
print(lst)
# [1, 2, 3, 4, [[3, 4, 5]], [3, 4, 5], 5, 6, [7, 8]]