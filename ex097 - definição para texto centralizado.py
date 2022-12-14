def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


# Programa principal
msg = str(input('Qual seu texto a centralizar? '))
escreva(msg)
escreva('Miguè mas Funciona!')