print('-=-' * 20)
velocidade = float(input('Qual a velocidade atual do automóvel? '))
print('-=-' * 20)
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é o de 80 km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('---Tenha um bom dia.Dirija com cuidado!---')