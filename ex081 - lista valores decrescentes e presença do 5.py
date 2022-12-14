valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resposta in 'n':
        break
print('=-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em orde decrescente são {valores}')
if 5 in valores:
    print('Valor 5 está presente na lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
