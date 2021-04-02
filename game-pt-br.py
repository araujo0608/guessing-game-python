from random import randint
import emoji

name = str(input('Digite seu nome: '))
print('\n')
print(emoji.emojize(':fire: :fire: :fire: BEM VINDO AO JOGO :fire: :fire: :fire:', use_aliases=True))
print('VOCÊ CONSEGUE ADIVINHAR QUE NUMERO ESTOU PENSANDO?')
print('DE 0 A 100')


number = randint(0, 100)
flag = False
attempts = 0

while flag == False:
    print(' ----------------- ')
    hunch = int(input('Seu palpite: '))

    if(hunch == number):
        flag = True
    else:
        attempts = attempts + 1
        if(hunch < number):
            #:arrow_up:
            print(emoji.emojize('É um numero maior que {} :arrow_up:'.format(hunch), use_aliases=True))
            #print('It is a number greater than {} '.format(hunch))
        if(hunch > number):
            # :arrow_down:
             print(emoji.emojize('É um numero menor que {} :arrow_down:'.format(hunch), use_aliases=True))

print('\n')
#:tada:
print(emoji.emojize(':tada: :tada: :tada:',use_aliases=True))
print('PARABÉNS {} VOCÊ ACERTOU ERA O NUMERO {}'.format(name,number))
#print('ATTEMPTS: {}'.format(attempts))
print(emoji.emojize('TENTATIVAS: {}  :trophy:'.format(attempts), use_aliases=True))
