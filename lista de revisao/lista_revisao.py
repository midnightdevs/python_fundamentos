# 1
def nome():
    print('leonardo')
nome()
# 2
numero = 1
print(type(numero))  
# 3
# Is a local where you can store a code, and pic it up in another part of the code.

# ------------------
# 1
numero1 = 6
numero2 = 2

soma = numero1 + numero2
print(soma)

# 2
divisao = numero1 / numero2
print(divisao)

# 3
divisao_resto = numero1 % numero2
print(divisao_resto)
# 4
# *

# ------------------

# 1
user = 'Leonardo'
print(f'Olá {user}')

# 2
for number in range(11):
    print(number)

# 3
# lists, tuple, range

# ------------------

# 1
lista = [1,2,3,4,5,6,7,8,9,10]

# 2
lista_minha = ['Leonardo',18,'Azul']

# 3
# store information in an orderly way.

# 4
lista1 = [1,2,3,4,5]
lista1.append(6)
print(lista1)

# 5
lista1.pop(1)
print(lista1)

# 6
lista_animais =  ['Leão', 'Pantera', 'Gato', 'Cachorro']
lista_animais.remove('Cachorro')
print(lista_animais)

# ------------------

# 1
tupla = ('João', 25)

nome_usuario = tupla.index('João')
print(nome_usuario)

nome_idade = tupla.index(25)
print(nome_idade)

# 2
# Não é possivel

# 3
# tuple is like a list but it is unchangeable

# 4
# the differece is that tuple is unchangeable and list you can change

# ------------------

# 1
vogais = {'a','e','i','o','u'}
alfabeto = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

igual = vogais.intersection(alfabeto)
print(igual)

# 2
conjunto1 = {1,2,3}
conjunto2 = {3,2,4,5}

# a uniao
uniao = conjunto1.union(conjunto2)
print(uniao)

# b itersecção
mesmo = conjunto1.intersection(conjunto2)
print(mesmo)

# c diferença
diferente = conjunto1.difference(conjunto2)
print(diferente)

# ------------------

# 1
um_dict = {
    'nome': 'Jonas',
    'idade': 25,
    'profissao':'Dev'
}
# 2
print(um_dict['nome'],um_dict['profissao'])

# 3
# um dicionario é uma especie de estrutura de dados do tipo coleção, nao sao acessados por posicao e indice igual as listas.
# A diferença é que conjunto é uma coleção de valores unicos.  

# ------------------

# 1
for atv in range(1,6):
    print(atv)

# 2



for pergunta in range(1):
    Nome1 = input('Qual o seu nome? ')
    idade1 = input('Qual a sua idade? ')
    genero = input('Qual o seu gênero? ')

outro_dict = {
    'Nome': Nome1,
    'Idade': idade1,
    'Gênero': genero
}

    # for pergunta in outro_dict:
    #     Nome1 = input('Qual o seu nome? ')
    #     idade1 = input('Qual a sua idade? ')
    #     genero = input('Qual o seu gênero? ')

print(outro_dict)
# ------------------

# 3

yes = input('Você Quer Começar? S/N ')


while yes == 'S':

    Nome2 = input('Qual o seu nome? ')
    idade2 = input('Qual a sua idade? ')
    profissao = input('Qual a sua profissão? ')
    yes = input('Você Quer continuar? S/N ')

    o_dict = {
        'Nome': Nome2,
        'Idade': idade2,
        'Profissão': profissao
    }
 lista_clientes = []
    dicionario = lista_clientes.append(o_dict)
print(dicionario)

# PORQUE AO CONSIGO MOSTRAR mAIS DE UM DICIONARIO************
# arrumar o local onde esta a lista