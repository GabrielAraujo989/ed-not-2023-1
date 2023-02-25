#Lista de numeros
nums = [9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

"""
Função que realiza uma busca sequencial em uma lista procurando por val.
Se val for encontrado, retorna a posição de val.
Caso contrario, retorna o valor -1.
"""

def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        #Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    #Percoreu toda a lista e não encontrou val: retorna -1
    return -1

###################################

#TESTES

#pROCURANDO O VALOR 15
resultado = busca_sequencial(nums, 15)
print(f"Posição do valor 15 na lista : {resultado}")

#pROCURANDO O VALOR 15
resultado = busca_sequencial(nums, 20)
print(f"Posição do valor 15 na lista : {resultado}")

#pROCURANDO O VALOR 15
resultado = busca_sequencial(nums, 33)
print(f"Posição do valor 15 na lista : {resultado}")


print("////" * 50)

#TESTE DE NOMES
#puxando a lsta de nomes de um arquivo externo

import sys
sys.dont_write_bytecode = True

from time import time
from data.lista_nomes import nomes
#Busca pelo nome 
hora_ini = time()
resultado = busca_sequencial(nomes, "GABRIEL")
hora_fim = time()
print(f"Posição do NOME GABRIEL : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

print("\o/" * 30)

hora_ini = time()
resultado = busca_sequencial(nomes, "YARA")
hora_fim = time()
print(f"Posição do NOME YARA : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

print("\o/" * 30)

hora_ini = time()
resultado = busca_sequencial(nomes, "CARLOS")
hora_fim = time()
print(f"Posição do NOME CARLOS : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

print("\o/" * 30)

hora_ini = time()
resultado = busca_sequencial(nomes, "PIKACHU")
hora_fim = time()
print(f"Posição do NOME PIKACHU : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print("\o/" * 30)