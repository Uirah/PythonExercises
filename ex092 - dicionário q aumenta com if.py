from datetime import datetime
trabalhador = {} #ou dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input(f'Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 para não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for key, value in trabalhador.items():
    print(f'  - {key} tem o valor {value}')
