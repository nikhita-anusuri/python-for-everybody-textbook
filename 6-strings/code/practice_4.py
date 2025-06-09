# f string allows python expressions to be used within string literals 
# wrapping a variable name with curly braces inside an f string
# will replace it with the value of the variable

# it returns the string '42'
camels = 42
print(f'{camels}')

print(f'I have spotted {camels} camels')

years = 3
count = .1
species = 'camels'
print(f'In {years} years I have spotted {count} {species}.')


