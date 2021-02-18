word = list('Delhi')
hidden =[]
for character in word:
    hidden.append('_')
#print(x)
#print(hidden)

attempts=0
max_attempts=4
isGameOver=False
while not isGameOver:
    print(f'you have {attempts-max_attempts} attempts remaining')
    hiddenString = ' '.join(hidden)
    print(f'The current word is : {hiddenString}')
    #break
    print('     ------')
    print('     |    |')
    print('     |    ' + ('O' if attempts > 0 else ''))
    print('     |    ' +('/\\' if attempts > 1 else ''))
    print('     |    ' +('|' if attempts > 2 else ''))
    print('     |    ' +('/\\' if attempts > 3 else ''))
    print(' --------')
    #break
    #letterGuessed =input('Please guess a letter: ')
    #break
    letterGuessed = input('Please guess a letter: ')

    print('\n\n\n\n')

    if letterGuessed in word:
        # if the player guessed correct, show all matched letters and print message
        print(f'You guessed correctly! {letterGuessed} is in the word')
        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = '_'
    else:
        # if player guessed wrong, print failure message and increment attempts
        print(f'You guessed wrong! {letterGuessed} is NOT in the word')
        attempts = attempts +1

    # if the player has won print a win message and stop looping
    if all('_' == char for char in word):
        print('Congrats, you won!')
        isGameOver = True

    # if the player has lost, print failing and stop looping
    if attempts >= max_attempts:
        print('You lost, rest in peace!')
        isGameOver = True
