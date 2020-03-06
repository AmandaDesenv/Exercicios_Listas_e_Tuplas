# Escreva uma função chamada intercala que recebe como entrada duas tuplas
# de três elementos cada e retorna uma tupla de seis elementos, intercalando
# as duas tuplas. Crie um módulo com essa função e importe esse módulo em
# outro programa. Neste outro programa, peça para o usuário preencher as duas
# tuplas, chame a função intercala e exiba o retorno da função.

import meus_modulos


tupla1 = ()
tupla2 = ()

for i in range(3):
    n1 = int(input("Digite um número: "))
    tupla1 = tupla1 + (n1,)


for i in range(3):
    n2 = int(input("Digite outro número:"))
    tupla2 = tupla2 + (n2,)


tupla3 = meus_modulos.intercala(tupla1, tupla2)
print(tupla3)
