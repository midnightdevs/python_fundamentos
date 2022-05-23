"""
Módulo de funções que usam argumentos.
"""

# Importando o módulo do sistema, para usarmos argumentos:
import sys

def funcao_principal():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    arg1 = sys.argv[1]
    print(arg1)

if __name__ == '__main__':
    funcao_principal()