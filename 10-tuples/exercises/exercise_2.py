fname = input("Enter a file name: ")
fhand = open(fname)

counts = {}
tuples_list = []
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    time = words[5]
    time_parts = time.split(':')
    hour = time_parts[0]
    counts[hour] = counts.get(hour, 0) + 1

for hour in counts:
    tuples_list.append((hour, counts[hour]))

tuples_list.sort()

for tuple in tuples_list:
    print(tuple[0], tuple[1])

# [('09', 2), ('18', 1)..]
