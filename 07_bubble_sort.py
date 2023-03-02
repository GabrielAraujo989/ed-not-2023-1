"""
Algoritimo de ordenação bobble sort
Percorre a lista a ser ordenada dem sucessivas passadas, trocando 2 elementos adjacentes sempre que o segundo for menor que o primeiro. Efetua tantas passadas quanto necessarias, até que, na ultima passada nenhuma troca seja feita.
"""
comps = trocas = passadas = 0

def bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    #Loop eterno, não sabemos quantas passadas serão necessarias

    while True:
        trocou = False

        #Percurso da lista, do primeiro ao penultimo elemento, com acesso a cada posição

        for pos in range(len(lista) - 1):

            comps += 1

            #Se o numero que está a frente na lista for menor do que o que esta atras, troca  suas posições
            
            if list[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] =lista[pos], lista[pos + 1]
                trocou = True
                trocas += 1
            if not trocou:   #se não ouvr troca na passada
                break         #Interrompe  o loop eterno; acabou

