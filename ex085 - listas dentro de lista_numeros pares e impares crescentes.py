numeros = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input((f'Digite {contador}º valor: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('=-' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
