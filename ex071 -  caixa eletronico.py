print('=' * 40)
print('{:^40}'.format('BANCO DEMONHO S.A.'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedulas = 200
totalcedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R${cedulas}')
        if cedulas == 200:
            cedulas = 100
        elif cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO DEMONHO S.A.! Tenha um bom dia!')

