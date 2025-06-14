name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
email_counts = {}
for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    email_counts[email] = email_counts.get(email, 0) + 1
 
max_count = 0 
max_email = None
for email in email_counts:
    if max_count < email_counts[email]:
        max_count = email_counts[email]
        max_email = email
print(email, max_count)