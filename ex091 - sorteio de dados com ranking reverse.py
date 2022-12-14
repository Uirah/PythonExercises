from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
#print(jogo)
print('Valores sorteados: ')
for key, value in jogo.items():
        print(f' O {key} tirou {value} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print(ranking)
print('-=' * 30)
print('      == RANKING DOS JOGADORES ==')
print()
for indice, valor in enumerate(ranking):
        print(f'        {indice + 1}º lugar: {valor[0]} com {valor[1]}')
        sleep(1)