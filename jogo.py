#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o resultado escolhido pelo computador. 
#O programa  deverá escrever na tela se o usuário venceu ou perdeu.(Curso em vídeo)

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




