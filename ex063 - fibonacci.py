print('-'*60)
print('{:^60}'.format('Sequência de Fibonacci'))
print('-'*60)
quantos = int(input('Quantos termos você quer mostrar? '))
print('~'*60)
t1 = 0
t2 = 1
print('{} >> {}'.format(t1, t2), end='')
count = 3
while count <= quantos:
    t3 = t1 + t2
    print(' >> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' >> FIM')
print('~'*60)
