"""
Meu primeiro módulo python.
"""

def funcao_principal():
    """
    A função principal do programa.
    """
    print('Olá Mundo')


def cadastro():
    nome = input('Informe o nome: ')
    sexo = input('Informe o sexo:')
    idade = int(input('Informe a idade: '))
    print('\n')

    return {
        "nome": nome,
        "sexo": sexo,
        "idade": idade
    }

def salva_clientes(num_clientes=3):
    lista_clientes = []
    for num in range(num_clientes):
        cliente = cadastro()
        lista_clientes.append(cliente)
    lista_clientes = ordena_por_idade(lista_clientes)

    return lista_clientes

def ordena_por_idade(lista_clientes):
    return sorted(lista_clientes, reverse = True, key=lambda d: d['idade'])


def outra_funcao():
    """
    Uma outra funcao dentro do programa.
    """
    print('Chamando outra função')

if __name__ == '__main__':
    lista_clientes = salva_clientes()
    print(lista_clientes)