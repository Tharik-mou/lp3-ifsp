valor = float(input('qual o valor da sua compra: '))

if valor >= 0.01 and valor <= 9.99:
    print(f'{valor}')
elif valor >= 10.00 and valor <= 99.99:
    valor -= (valor * 5 / 100)
    print(f'{valor}')
elif valor >= 100.00 and valor <= 499.99:
    valor -= (valor * 10 / 100)
    print(f'{valor}')
else:
    valor -= (valor * 15 / 100)
    print(f'{valor}')

