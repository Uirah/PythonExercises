listanum = []
maior = menor = 0
for contador in range(0, 5):
    listanum.append(int(input(f'Digite un valor para a posição {contador}: ')))
    if contador == 0:
        maior = menor = listanum[contador]
    else:
        if listanum[contador] > maior:
            maior = listanum[contador]
        if listanum[contador] < menor:
            menor = listanum[contador]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end='')
print()
