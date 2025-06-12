users_list = []

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    users_list.append(float(num))

print(f'Maximum: {max(users_list)}')
print(f'Minimum: {min(users_list)}')
      
# a.method1()
# fun1(a)