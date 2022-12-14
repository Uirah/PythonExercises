aluno = {} #ou dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 30)
print(aluno)
print(aluno['média'])
if aluno['média'] >= 7:
    aluno['situação'] = str('Aprovado')
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação' #pode não colocar str
else:
    aluno['situação'] = str('Reprovado')
for key, value in aluno.items():
    print(f'  - {key} é igual a {value}')