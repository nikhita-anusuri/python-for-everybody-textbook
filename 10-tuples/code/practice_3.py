# tuple assignment

m = ('have', 'fun')
# assigning variables values using a tuple
x, y = m
print(x)
print(y)

m = ['have', 'fun']
x, y = m
print(x)
print(y)

m = ('have', 'fun')
x = m[0]
y = m[1]
print(x)
print(y)

m = ('have', 'fun')
(x, y) = m
print(x)
print(y)

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)