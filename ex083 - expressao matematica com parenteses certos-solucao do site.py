expressao = str(input('Digite uma expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() #remove o item da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está incorreta. Verifique o que foi digitado.')