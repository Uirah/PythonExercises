from random import randint
vitorias = 0
print('=-' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
while True:
    print('=-' * 20)
    valor = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = valor + computador
    p_ou_i = ' '
    while p_ou_i not in 'PI':
        p_ou_i = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 40)
    print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}... ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if p_ou_i == 'P':
        if soma % 2 == 0:
            print ('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif p_ou_i == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=-' * 20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
