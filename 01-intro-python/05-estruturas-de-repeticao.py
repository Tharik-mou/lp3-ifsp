# for, while (break/continue)

# for
for letra in 'Hello World':
    print(letra)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# range 
for i in range(5):
    print(i)

# 0 até 100
lista = list(range(101))
print(lista)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break

comando = ''

while True:
    comando = input('Digite o comando')
    if comando == 'sair':
        break
    if comando == '1':
        print('1')

# continue
numeros = [-10, 3, 0, 5, -2]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

# compreensao de listas
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrado = numero ** 2
    quadrados.append(quadrado)

quadrados = [numero ** 2 for numero in numeros]

numeros = [-3, 0, -5, 1, 2, 4]
positivos = [numero for numero in numeros if numero > 0]
