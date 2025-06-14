# dictionaries and tuples
# turning dictionary into tuple
# method named items returns a list of tuples
d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
print(t)

t.sort()
print(t)

d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val, key)

l = list()
for key, val in d.items():
    l.append((val, key))

print(l)

l.sort(reverse=True)
l
