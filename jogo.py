import random
from time import sleep
computador=random.randint(0,5)
print('-=-' *20)
print('Pensarei em um número entre 0 e 5. Adivinhe se puder!')
print('-=-' *20)
jogador= int(input('Em qual número pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! você acertou.')
else:
    print('Você errou! Pensei no número {} e não no {}'.format(computador,jogador))
print('---Gamer Over---')




