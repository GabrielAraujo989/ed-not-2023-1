"""
ALGORITIMO DE ORIENTAÇÃO SELECT SORT

Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor valor no restante da lista Se o valor encontrado for menor que o valor previamente selecionado, efetua a troca entre eles. Continuando, seleciona o segundo elemento da lista, buscando pelo menor valor das posições subsequentes Faz a troca entre os dois valores, se necessário. O processo se repete até que o penúltimo elemento da lista seja isolado, comparado com o último e feita a troca entre eles, se for o caso.

"""
comps = trocas = passadas = 0

def selection_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0
# loop que vai da primeira a penultima posição
    for pos_sel in range(len(lista) - 1):
        passadas += 1
        #Encontra o menor valor na sublista á frente de pos-sel
        pos_menor = pos_sel + 1
        for pos in range(pos_sel + 2, len(lista)):
            #Se o valor encontrado na posição pos for menor que o valor da posição pos_menor, então pos_menor passa a ser pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        #Compara os elementos das posições pos_menor e pos_sel. Se o valor do primeiro for menor que o valor do segundo, efetua a troca
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
        trocas += 1
########################################################################################################

nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7, 33, 44, 11, 10, 54, 65, 30, 33, 12, 14, 20]

selection_sort(nums)
print("Lista odenada: ", nums)
print(f"Comparações: {comps}, Trocas: {trocas}, passadas: {passadas}")


#####################################################################################################

from time import time
import sys
sys.dont_write_bytecode = True

from data.nomes_desord import nomes

nomes = nomes[:10000]

horaini = time()
selection_sort(nomes)
horafim = time()

print("Nomes ordenados: ", nomes)
print(f"Tempo gasto: {(horafim - horaini) * 1000}ms")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")