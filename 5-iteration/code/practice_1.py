# flow of a while loop
# evaluate condition
# if condition true execute body
# if condition false exit the while loop and continue executing code
# 5 iterations means body of loop was executed 5 times

n = 3
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')


# loop runs until line = done
# loop ends by using a break statement

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

# break statement breaks loop
# continue statement moves to next iteration immediately