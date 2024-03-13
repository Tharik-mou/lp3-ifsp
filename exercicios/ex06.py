comprimento = float(input('Digite o comprimento do seu: '))
altura = float(input('Digite a altura do seu: '))
largura = float(input('Digite a altura do seu: '))
temperatura_ambiente = int(input('Digite a temperatura ambiente: '))
temperatura_desejada = int(input('Digite a temperatura desejada: '))

def volume_aquario(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def potencia_termostato(volume, temperatura_ambiente, temperatura_desejada):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def filtragem(volume):
    return volume * 2, volume * 3

volume = volume_aquario(comprimento, altura, largura)
print(f'{volume}')
print(f'{potencia_termostato(volume, temperatura_ambiente, temperatura_desejada)}')
print(f'{filtragem(volume)}')

