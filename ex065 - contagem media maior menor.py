n = soma = count = media = maior = menor = 0
quer = 'S'
while quer in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    count += 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    quer = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / count
print('Você digitou {} números e a média foi {}'.format(count, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
