print('-' * 40)
print('{:^40}'.format('LOJA TABAJARA'))
print('-' * 40)
menor = contador = caro = total = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    contador += 1
    total += preco
    if preco > 1000:
        caro += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = prod
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('-' * 40)
        break
print('{:-^40}'.format(' FIM DA COMPRA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')