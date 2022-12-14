valores = []
pares = []
impares =[]
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resposta in 'n':
        break
for indice, valor in enumerate(valores):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('=-' * 30)
print(f'A lista completa é {valores}')
pares.sort()
print(f'Os valores pares são {pares}')
impares.sort()
print(f'Os valores impares são {impares}')
