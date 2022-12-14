from random import randint
from time import sleep
lista = []
jogosPC = []
print('-' * 50)
titulo= 'JOGAR NA MEGA SENA'
print(titulo.center(50))
print('-' * 50)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
totaljogos= 1
while totaljogos <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contagem += 1
        if contagem >= 6:
            break
    lista.sort()
    jogosPC.append(lista[:])
    lista.clear()
    totaljogos += 1
print()
print('-=' * 8, f'SORTEANDO {quantidade} JOGOS', '-=' * 8)
print()
for indice, listagem in enumerate(jogosPC):
    print(f'Jogo {indice + 1}: {listagem}')
    sleep(1)
print()
print('-=' * 8, '< BOA SORTE! >', '-=' * 8)
