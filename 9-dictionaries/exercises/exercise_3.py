file_name = input("Enter file name: ")
fhandler = open(file_name)
emails = {}
for line in fhandler:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    emails[email] = emails.get(email, 0) + 1
print(emails)