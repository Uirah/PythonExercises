print('=' * 40)
print('{:^40}'.format('BANCO DEMONHO S.A.'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
guara = garoupa = onca = mico = arara = garca = tartaruga = beijaflor = 0
resto1 = resto2 = resto3 = resto4 = resto5 = resto6 = resto7 = 0

if valor >= 200:
    guara = valor // 200
    resto1 = valor % 200
for valor in range(100, 200) or resto1 in range(100, 200):
    valor1 = valor
    garoupa = valor1 // 100
    resto2 = valor1 % 100
for valor in range(50, 100) or resto2 in range(50, 100):
    valor2 = valor
    onca = valor2 // 50
    resto3 = valor2 % 50
for valor in range(20, 50) or resto3 in range(20, 50):
    valor3 = valor
    mico = valor3 // 20
    resto4 = valor3 % 20
for valor in range(10, 20) or resto4 in range(10, 20):
    valor4 = valor
    arara = valor4 // 10
    resto5 = valor4 % 10
for valor in range(5, 10) or resto5 >= 5:
    valor5 = valor
    garca = valor5 // 5
    resto6 = valor5 % 5
for valor in range(2, 5) or resto6 >= 2:
    valor6 = valor
    tartaruga = valor6 // 2
    resto7 = resto6 % 2
if valor == 1 or resto7 == 1:
    beijaflor = 1
if guara > 0:
    print(f'Total de {guara} cédulas de R$200')
if garoupa > 0:
    print(f'Total de {garoupa} cédulas de R$100')
if onca > 0:
    print(f'Total de {onca} cédulas de R$50')
if mico > 0:
    print(f'Total de {mico} cédulas de R$20')
if arara > 0:
    print(f'Total de {arara} cédulas de R$10')
if garca > 0:
    print(f'Total de {garca} cédulas de R$5')
if tartaruga > 0:
    print(f'Total de {tartaruga} cédulas de R$2')
if beijaflor > 0:
    print(f'Total de {beijaflor} cédula de R$1')
