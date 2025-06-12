s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
print(delimiter.join(t))

# append method modifies a list
# but the + operator creates a new list
# slicing creates a new list
