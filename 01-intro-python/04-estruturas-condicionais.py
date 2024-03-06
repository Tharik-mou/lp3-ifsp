# if, if/else, if/elif/else, ternario, match

# if 
# if condicao:
#     codigo do if

idade = 20
if idade >= 18:
    print('maioridade')

print('fora do if')

# if / else
if idade >= 18:
    print('maioridade')
else: 
    print('menoridade')

# if/elif/else

idade = 30
if idade <= 12:
    print()
elif idade <= 17:
    print()
elif  idade <= 59:
    print()
else:
    print()

# evitar aninhamento de ifs

email = ''
senha = ''

if email == 'admin@email.com':
    if senha == '123admin':
        print('liberado')
    else:
        print('email ou senha incorretos')
else:
    print('email ou senha incorretos')

if email == 'admin@email.com' and senha == '123admin':
    print('liberado')
else:
    print('senha ou email incorretos')


# entrada numero 1, 2, 3 ...7
# saida dia: Domingo, Segunda, Terça ...Sabado

dia = 4
dias = {
    1 : 'domingo',
    2 : 'segunda',
    3 : 'terça',
    4 : 'quarta',
    5 : 'quinta',
    6 : 'sexta',
    7 : 'sabado'
}

if dia in dias:
    print(dias[dia])
else:
    print('dia invalido')

# ternario

media = 8.0

if media >= 6.0:
    situacao = aprovado
else:
    situacao = 'reprovado'

situacao = 'aprovado' if media >= 6.0 else 'reprovado'

# match

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabado')
    case _:
        print('invalido')

# dia util 2, 3, 4, 5, 6
# fds: 1, 7

match dia:
    case 1 | 7:
        print('fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia util')
    case _:
        print('invalido')


