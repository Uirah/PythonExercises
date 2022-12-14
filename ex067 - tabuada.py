while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if valor < 0:
        break
    for count in range(1, 11):
        print(f'{valor} x {count} = {valor * count}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
