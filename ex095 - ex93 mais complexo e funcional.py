time = []
jogador = {} #ou dict()
totalgols = list() # ou []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totalgols.clear()
    for contador in range(0, partidas):
        totalgols.append(int(input(f'    Quantos gols na partida {contador + 1}? ')))
    jogador['gols'] = totalgols[:]
    jogador['total'] = sum(totalgols)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resposta == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for indice in jogador.keys():
    print(f'{indice:<15}', end='')
print()
print('-' * 40)
for key, value in enumerate(time):
    print(f'{key:>3} ', end='')
    for dado in value.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for indice, golzitos in enumerate(time[busca]['gols']):
            print(f'    No jogo {indice + 1} fez {golzitos} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice + 1}, {jogador["nome"]} fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
