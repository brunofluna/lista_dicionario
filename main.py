# tupla
chaves = ('Nome', 'Idade', 'Profissão')

# lista de dicionários
usuarios = [
    {
    chaves[0]: 'Fulano',
    chaves[1]: 20,
    chaves[2]: 'Programador'
    },
    {
    chaves[0]: 'Ciclano',
    chaves[1]: 35,
    chaves[2]: 'Analista'
    },
    {
        chaves[0]: 'Beltrano',
        chaves[1]: 45,
        chaves[2]: 'Faxineiro'
    }
]

#mostrar a lista de usuários na tela

print(f'{'='*10} LISTA DE USUÁRIOS {'='*10}\n')
for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{'-'*10}\n')

# adcionar novo dicionarios à lista
usuario = {}

for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'Informe {chaves[i]}: ')

usuarios.append(usuario)
print(f'\nUsuário cadastrado com sucesso!')

#Reexibindo a nova lista de usuário
print(f'{'='*10} LISTA DE USUÁRIOS {'='*10}\n')
for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{'-'*10}\n')
    

#comentei para entender o conceito,
# # Lista de dicionarios
# usuarios = [
#     {
#     'Nome': 'Fulano',
#     'Idade': 20,
#     'Profissão': 'Programador'
#     },
#     {
#     'Nome': 'Ciclano',
#     'Idade': 35,
#     'Profissão': 'Analista'
#     },
#     {
#         'Nome': 'Beltrano',
#         'Idade': 45,
#         'Profissão': 'Faxineiro'
#     }
# ]