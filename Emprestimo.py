'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa. O salário do comprador e em quantos anos pretende pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário. Caso isso ocorra
o empréstimo será negado.
'''

valor_casa = float(input('Digite o valor da casa R$:'))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos pretende pagar?'))

prest = valor_casa /(anos * 12)
cal_salario = (salario*30)/100

if prest > cal_salario:
    print('Infelizmente seu empréstimo foi negado!')
else:
    print('Parabéns seu empréstimo foi liberado! Você pagará por uma casa de R${:.2f} em {} anos com  uma prestação de R${:.2f}'.format(valor_casa,anos, prest))