file_name = input("Enter file name: ")
fhandler = open(file_name)
email_counts = {}
for line in fhandler:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    email_counts[email] = email_counts.get(email, 0) + 1

maximum = 0
max_email = None
for email in email_counts:
    if email_counts[email] > maximum:
        maximum = email_counts[email]
        max_email = email
print(max_email, maximum)