# Operadores
# aritmeticos
# +, -, /, *, %

nota1 = 10
nota2 = 3
media = (nota1 + nota2) / 2

# potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado

# logicos
# and, or, not
# acesso liberado = nao bloqueado , idade > 18, horario comercial
bloqueado = False
idade = 21
hora_atual = 10

maioridade = idade > 18
horario_comercial = hora_atual > 8 and hora_atual <= 18

if not bloqueado and maioridade and horario_comercial:
    print('liberado')
else:
    print('nao liberado')

verdade = True and False

# operadores de comparação
# >, <, >=, <=, ==, =!
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) # True

# operador is
print(numeros is numeros2) # False
numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) # True
print(numeros3 is not numeros4) # False

# in = (bool)
print('a' in 'Python') # False

prontuarios = ['SP3090078', 'SP3456778', 'SP0845638']
prontuario = 'SP3090078'
print(prontuario in prontuarios) # True

# sim, não, talvez
opcao = ''
if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opcao valida')
else:
    print('opcao invalida')

opcoes = ('sim', 'nao', 'talvez')
if opcao in opcoes:
    print('opcao valida')
else:
    print('opcao invalida')