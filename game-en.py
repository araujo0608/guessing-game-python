from random import randint
import emoji

name = str(input('Type your name: '))
print('\n')
print(emoji.emojize(':fire: :fire: :fire: WELCOME TO THE GAME :fire: :fire: :fire:', use_aliases=True))
print('YOU CAN GUESS WHAT NUMBER I AM THINKING OF')
print('FROM 0 TO 100')


number = randint(0, 100)
flag = False
attempts = 0

while flag == False:
    print(' ----------------- ')
    hunch = int(input('Your guess: '))

    if(hunch == number):
        flag = True
    else:
        attempts = attempts + 1
        if(hunch < number):
            #:arrow_up:
            print(emoji.emojize('It is a number greater than {} :arrow_up:'.format(hunch), use_aliases=True))
            #print('It is a number greater than {} '.format(hunch))
        if(hunch > number):
            # :arrow_down:
             print(emoji.emojize('It is a number smaller than {} :arrow_down:'.format(hunch), use_aliases=True))

print('\n')
#:tada:
print(emoji.emojize(':tada: :tada: :tada:',use_aliases=True))
print('CONGRATULATIONS {} YOU GOT THE NUMBER {} RIGHT'.format(name,number))
#print('ATTEMPTS: {}'.format(attempts))
print(emoji.emojize('ATTEMPTS: {}  :trophy:'.format(attempts), use_aliases=True))
