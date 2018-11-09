#Curso solid prof: Guilherme Junqueira

'''
Exercício: Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decida se ela está apta a ser do exercito. (Para entrar
no no exercito é preciso ter mais de 18 anos e pesar mais de 60 kilos e
medir mais ou igual a 1.70 metros.
'''

print('----------Ingresso no Exercito----------')
idade = int(input('Digite sua idade: '))
peso = int(input('Digite seu peso: '))
altura = int(input('Digite sua altura: '))

if idade >= '18' and peso >= '' and altura >= '1.7':
    print('Você está apto a ingressar no Exercito')
else:
    print('Você não está apto a ingressar no Exercito')
