numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))

notas = [numero1, numero2, numero3]

media = sum(notas) / len(notas)

print(f'o valor da media é {media}')