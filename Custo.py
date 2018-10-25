#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$ 0, 50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.

print('-=-' * 20)
distan= float(input('Digite a distância (km) que será percorrida na viagem: '))
print('-=-' * 20)
if distan <= 200:
    print('Seu gasto será de {}'.format(distan* 0.50))
else:
    print('Seu gasto será de {}'.format(distan * 0.45))
print('----BOA VIAGEM!----')