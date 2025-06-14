t = ('a', 'b', 'c', 'd', 'e')
# to create a tuple with a single element
t1 = ('a',)
print(type(t1))

# another way to make a tuple
t = tuple()
print(t)

t = tuple('lupins')
print(t)
print(t[0])
print(t[1:3])

t = ('a', 'b', 'c', 'd', 'e')

t = ('A',) + t[1:]
print(t)

# comparing tuples

