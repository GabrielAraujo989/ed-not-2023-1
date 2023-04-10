"""
  ALGORITMO DE ORDENAÇÃO BUBBLE SORT
  Percorre a lista a ser ordenada em sucessivas passadas,
  trocando dois elementos adjacentes sempre que o segundo
  for MENOR que o primeiro. Efetua tantas passadas quanto
  necessárias, até que, na última passada, nenhuma troca
  seja efetuada
  VERÇÃO OTIMIZADA
"""

# Variáveis de estatística
comps = trocas = passadas = 0

def bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0
    desloc = 1
    
    # Loop eterno, não sabemos quantas passadas serão
    # necessárias
    while True:
        trocou = False
        passadas += 1

        # Percurso da lista, do primeiro ao PENÚLTIMO
        # elemento, com acesso a cada posição
        for pos in range(len(lista) - desloc):
            
            comps += 1
            
            # Se o número que está à frente na lista
            # for MENOR do que o que está atrás, TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
                trocas += 1
                

        if not trocou:  # Não houve troca na passada
            break       # Interrompe o loop eterno; acabou

        desloc += 1
#############################################################################

nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7, 33, 44, 11, 10, 54, 65, 30, 33, 12, 14, 20]

bubble_sort(nums)
print("Lista odenada: ", nums)
print(f"Comparações: {comps}, Trocas: {trocas}, passadas: {passadas}")

pior_caso = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

bubble_sort(pior_caso)
print("Lista odenada: ", pior_caso)
print(f"Comparações: {comps}, Trocas: {trocas}, passadas: {passadas}")

melhor_caso = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

bubble_sort(melhor_caso)
print("Lista odenada: ", melhor_caso)
print(f"Comparações: {comps}, Trocas: {trocas}, passadas: {passadas}")

##########################################################################################

from time import time
import sys
import tracemalloc
sys.dont_write_bytecode = True

from data.nomes_desord import nomes

nomes = nomes[:10000]
tracemalloc.start()
horaini = time()
bubble_sort(nomes)
horafim = time()

men_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", nomes)
print(f"Tempo gasto: {(horafim - horaini) * 1000}ms")
print(f"Pico de memoria: {mem_pico / 1024 / 1024} MB")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")
