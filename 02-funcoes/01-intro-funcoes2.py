# Função
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funcionalidades)

# Declaração
def ola_mundo():
    print('Olá Penis')

# Chamada
ola_mundo()
ola_mundo()

# Função sem retorno
# Side effect - Efeito colateral
def imprimir_mensagem(nome):
    print(f'Bom dia, {nome}')

imprimir_mensagem('ROGERINHO DO MORRO')

# Função com retorno
# Função pura
def mensagem(nome):
    return f'Bom dia, {nome}'

print(mensagem('Maria'))

# Parâmetro e Argumentos
def somar(numero1, numero2):
    return numero1 + numero2

somar(10.0, 3.4)

# Escopo de variáveis
def media(nota1, nota2, nota3):
    return nota1 + nota2 + nota3 / 3

# Parametros com valor padrão
def mensagem(nome, mensagem = 'Bom dia'):
    return f'{mensagem}, {nome}'

mensagem('Mario', 'Bom dia')

# Argumentos nomeados
print('Olá', '123', 'teste', sep = '@', end = '\n\n')
print('TESTE')

mensagem(nome = 'Lucas', mensagem = 'Boa Tarde')

# Docstring

def somar(n1, n2):
    """Função q soma dois numeros meu fi
    
    :param n1: primeiro numero
    :param n2: segundo numero
    :return : soma dos numeros
    """
    return n1 + n2

somar(2, 3)

# Funções built-in
# Print, type, min, max, int, str, input, len, sum

def media(*notas):
    return sum(notas) / len(notas)

media(10.0, 3.5, 7.5)