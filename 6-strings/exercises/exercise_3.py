word = 'banana'
count = word.count('a')
print(count)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

# using a version of find that allows us to specify a position in the string
# where it should start looking
