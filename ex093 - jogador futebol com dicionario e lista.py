jogador = {} #ou dict()
totalgols = list() # ou []
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for contador in range(0, partidas):
    totalgols.append(int(input(f'    Quantos gols na partida {contador + 1}? ')))
jogador['gols'] = totalgols[:]
jogador['total'] = sum(totalgols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice + 1}, {jogador["nome"]} fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
