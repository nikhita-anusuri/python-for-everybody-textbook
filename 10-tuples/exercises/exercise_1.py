fname = input("Enter a file name: ")
fhand = open(fname)

message_count = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    message_count[email] = message_count.get(email, 0) + 1


counts_list = []
for email, count in message_count.items():
    counts_list.append((count, email))

counts_list.sort(reverse=True)
most_emails = counts_list[0]
print(most_emails[1], most_emails[0])

