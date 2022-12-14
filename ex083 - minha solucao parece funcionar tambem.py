expressao = str(input('Digite uma expressão: '))
abres = fechas = 0
for simbolos in expressao:
    if simbolos == '(':
        abres += 1
    elif simbolos == ')':
        fechas += 1
if abres == fechas:
    print('A expressão está válida!')
else:
    print('A expressão está incorreta. Verifique o que foi digitado.')