counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

lst = list(counts.keys())
print(lst)
lst.sort()
print(lst)
for key in lst:
    print(key, counts[key])

