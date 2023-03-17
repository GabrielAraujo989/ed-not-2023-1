"""
ALGORITIMO DE ORDENAÇÃO MERGE SORT

no processo de ordenação, esse algoritimo "desmonta" a lista original, contendo N elementos, até obter N listas com apenas um elemento cada uma. Em seguida, usando a técnica de mesclagem (merge), "remonta" a lista, desta vez com os elementos ja em ordem.
"""
#Variaveis de estatistica
divs = juncs = comps = 0
def merge_sort(lista):

    global divs, juncs, comps
    #Para que possa aver divisão da lista, esta deve ter mais de um elemento
    if len(lista) > 1:

        #Encontra a posição do meio da lista, para fazer a divisão em duas metades
        meio = len(lista) // 2

        #Tira uma copia da primeira metade da lista 
        sublista_esq = lista[:meio]
        #tira uma copia da segunda metade da lista
        sublista_dir = lista[meio:]
        divs += 1 # Numero de divisoes

        #Chamamos recursivamente a função para que ela continue repartindo cada uma das sublistas em duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)
        
        #AQUI COMEÇA A MESCLAGEM ORDENADA DAS SUBLISTAS 
        pos_esq = pos_dir = 0
        ordenada = []

        #Compara os elementos das sublistas entre si e insere na lista ordenada o menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
            #O menor elemento está na sublista da esquerda
            comps += 1    #Numero de composições
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                #"Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1 #Incrementa pos_esq
                #O menor elemento está na sublista da direita
            else:
                #Desce o elemento da direita para a sublista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1   #Incrementa pos_dir
         
        #Verificação de sobra
        sobra = []   #Lista vazia

         #Sobra a esquerda
        if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]
        #Sobra da direita
        else: sobra = sublista_dir[pos_dir:]


        juncs += 1  #numero de junções

        #resultado final é a junção (concatenação) da lista ordenada com sobra
        return ordenada + sobra
    else:
        return lista

##############################################

# Teste com vetor de 10 numeros

nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]

#Resta as variaveis de estatistica
divs = juncs = comps = 0
resultado = merge_sort(nums)
print("Lista original: ", nums)
print("Lista ordenada: ", resultado)
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")

