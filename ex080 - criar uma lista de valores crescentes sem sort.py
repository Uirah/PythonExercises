# eu tinha nem ideia de como fazer isso
lista = []
for contador in range(0, 5):
    n = int(input('Digite um valor: '))
    if contador == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
