num=list()
men=0
mai-0
while True:
    n=int(input('Digite um numero: '))
    if n not in num:
        num.append(n)
        print('Numero adicionado com sucesso...')
    else:
        print('esse numero ja esta cadastrado..')
    r=str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        print('Fim do programa')
print('-='*30)
print(f'Voce digitou {num}')
