
x = 10
y = 11

# instead of doing this:

if 0 < x: 
    if x < 10:
        print('x is a positive single digit number.')

# this uses the and operator
if 0 < x and x < 10:
    print('x is a positive single digit number.')