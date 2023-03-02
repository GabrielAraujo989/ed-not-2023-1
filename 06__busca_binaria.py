"""
ALGORITIMO DE BUSCA BINARIA
Dados uma lista, que  deve estar preveamente ordenada, e um valor de busca, divide a llista em duas metades procurando o valor de busca apenas na metade onde o valor poderia estar. Novas subdivisoes são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando então se conclui que o valor de busca não existe na lista.


comps = 0 # conta o numero de conparações
def busca_binaria(lista, val):
    global comps
    comps = 0

    ini = 0     # inicio da lista
    fim = len(lista) - 1    #Fim da lista

    while ini <= fim:
        meio = (ini + fim) / 2  #divisão inteira para achar o o numeri inteiro no meio da lista

    #) valor de busca foi encontrado
    # Retorna a posição
    if lista[meio] == val: 
        comps += 1
        return meio
    elif val < lista[meio]:
        comps += 2
        fim = meio - 1               # a posição do inicio e do fim da lista muda de acordo com o   
    else: #val > lista[meio]:       #valor de meio
        ini = meio + 1

    return -1 # quando o valor não existe na lista

"""
"""
  ALGORITMO DE BUSCA BINÁRIA
  Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
  e um valor de busca, divide a lista em duas metades
  procurando pelo valor de busca apenas na metade onde
  o valor poderia estar. Novas subdivisões são feitas
  até que se encontre o valor de busca ou que reste
  apenas uma sublista vazia, quando então se conclui
  que o valor de busca não existe na lista.
"""
comps = 0       # Conta o número de comparações
def busca_binaria(lista, val):
    global comps
    comps = 0

    ini = 0               # Início da lista
    fim = len(lista) - 1  # Fim da lista

    while ini <= fim:
        meio = (ini + fim) // 2     # Divisão inteira

        # O valor de busca foi encotrado.
        # Retorna a posição
        if lista[meio] == val: 
            comps += 1
            return meio

        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        else: # val > lista[meio]
            comps += 2
            ini = meio + 1

    return -1   # valor não existe na lista


import sys
sys.dont_write_bytecode = True

from time import time
from data.lista_nomes import nomes
#Busca pelo nome 
hora_ini = time()
resultado = busca_binaria(nomes, "GABRIEL")
hora_fim = time()
print(f"Posição do NOME GABRIEL : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

print("\o/" * 20)

hora_ini = time()
resultado = busca_binaria(nomes, "YARA")
hora_fim = time()
print(f"Posição do NOME YARA : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

print("\o/" * 20)

hora_ini = time()
resultado = busca_binaria(nomes, "CARLOS")
hora_fim = time()
print(f"Posição do NOME CARLOS : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")

print("\o/" * 20)

hora_ini = time()
resultado = busca_binaria(nomes, "PIKACHU")
hora_fim = time()
print(f"Posição do NOME PIKACHU : {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")


print("\o/" * 20)


#Busca pelo nome AARAO
hora_ini = time()
resultado = busca_binaria(nomes, "AARAO")
hora_fim = time()
print(f"Posição do nome AARAO na lista: {resultado}")
print(f"Tempo Gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {comps}")