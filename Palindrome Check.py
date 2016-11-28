
x = input('Type a word to see if it is a palindrome ')


if x.lower() == (x[::-1]):
    print('')
    print(str(x.lower()) + ' Backwards is... ' + str(x[::-1]))
    print('')
    print(str(x.lower()) + ' is a palindrome!')
else:
    print('Sorry ' + str(x.lower()) + ' Is not a palindrome!')
