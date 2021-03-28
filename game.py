from random import randint

name = str(input('Type your name: '))
print(10 * '*')
print('*** WELCOME TO THE GAME ***')
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
            print('It is a number greater than {} '.format(hunch))
        if(hunch > number):
            print('It is a number smaller than {} '.format(hunch))

print('CONGRATULATIONS {} YOU GOT THE NUMBER {} RIGHT'.format(name,number))
print('ATTEMPTS: {}'.format(attempts))
