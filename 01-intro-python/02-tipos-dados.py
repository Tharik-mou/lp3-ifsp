# Tipos de dados

# Numerico

# int
idade = 10

# float
idade = 61.90

# booleano
# True, False
verdade = False
mentira = True

# String = str
# sequencia de caracteres
# literal de str
nome = 'José'
nome = "José"

# char 
letra = 'a'

frase = """
Olá pessoal
teste
teste
"""

# interpolação de String
nome = 'Sônia'
idade = 23
mensagem = f'Bom dia {nome}. Você tem {idade} anos'

nome = 'Silvio Santos'
print(nome[2])


# list
# lista de valores
# pode conter valores de tipos diferentes
# podem ser alteradas(adicionar, remover)

habilidades = ['java', 'html', 'css']
print(habilidades [0])

habilidades[0] = 'javascript'
print(habilidades)

habilidades.append('python')
print(habilidades)

habilidades.insert(0, 'kotlin')
print(habilidades)

# remove, sort, clear, copy ...

for habilidade in habilidades: 
    print(habilidade)

#tuple
# lista de valores
# nÕ PODE ALTERAR OS VALORES
opcoes = ('sim', 'não', 'talvez')
racas_rpg = ('anao', 'humano', 'elfo')

print(opcoes[1])

# funcao que retorna estatisticas
#media, a menor, a maior

def estatistica_nota(notas):
    media = sum(notas) / len(notas) 
    menor = min(notas)
    maior = max(notas)

    return media, menor, maior

notas = [10.0, 5.5, 3.2, 1.8]
estatistica = estatistica_nota(notas)
print(estatistica)
print(type(estatistica))


media, menor, maior = estatistica_nota(notas)
print(media, menor, maior, True, 1.2)

# set
# conjunto de valores
# não permite valores duplicados 
# não é indexado

habilidades = {'java', 'python', 'css'}
habilidades.add('java')
print(habilidades)

# dict
# palavras
pessoa = {
    'nome': 'Silvio Santos',
    'casado': True,
    'idade': 120
}

print(pessoa['nome'])
print(pessoa['casado'])
print(pessoa['idade'])

pessoa['rico'] = True

print(pessoa)

nulo = None
