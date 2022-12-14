maiores = homens = meninas = 0
print('-' * 40)
print('{:^40}'.format('CADASTRE UMA PESSOA'))
while True:
    print('-' * 40)
    sexo = continuar = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        meninas += 1
    print('-' * 40)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('-' * 40)
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {meninas} mulheres com menos de 20 anos.')
