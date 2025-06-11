t = ['a', 'b', 'c']
x = t.pop()
print(t)
print(x)

x = t[1]
del t[1]
print(t)
print(x)

x = ['a', 'b', 'c']
x.remove('b')
print(x)

y = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
