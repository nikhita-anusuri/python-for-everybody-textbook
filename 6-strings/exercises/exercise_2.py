def character_count(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)

character_count('banana', 'a')
# function gets count of a specific character in a word