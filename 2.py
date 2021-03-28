import random

score = 10
true_chars = []
words = ['cat', 'Student', 'Dark', 'Python',
         'Star', 'Orange', 'Zebra', 'Iran', 'Paper']
word = random.choice(words)
while True:
    strtemp = ''

    for i in range(len(word)):
        if word[i].lower() in true_chars:
            print(word[i], end='')
            strtemp += word[i]
        else:
            print('-', end='')
    if word == strtemp:
        print('\n Congratulations! you win')
        break
    char = input('\nplease enter a character: ')

    if char.lower() in word.lower():
        true_chars.append(char)
    else:
        score -= 1
    print(score)

    if score == 0:
        print("Game Over!")
        break
