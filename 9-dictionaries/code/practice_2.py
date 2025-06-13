counts = [ 0 for i in range(26) ]

string = "abcdecdba"
for char in string:
    index = ord(char) - ord('a')
    counts[index] += 1

print(counts)