file_name = input("Enter file name: ")
fhandler = open(file_name)
domain_counts = {}
for line in fhandler:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    email_parts = email.split("@")
    domain = email_parts[1]
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

print(domain_counts)