nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

elements = []

while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    num = float(inp)
    elements.append(num)
print(sum(elements)/len(elements))
