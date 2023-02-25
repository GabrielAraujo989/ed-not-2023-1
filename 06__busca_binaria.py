"""
ALGORITIMO DE BUSCA BINARIA
Dados uma lista, que  deve estar preveamente ordenada, e um valor de busca, divide a llista em duas metades procurando o valor de busca apenas na metade onde o valor poderia estar. Novas subdivisoes são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando então se conclui que o valor de busca não existe na lista.

"""
comps = 0 # conta o numero de conparações
def busca_binaria(lista, val):
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
        fim = meio -                # a posição do inicio e do fim da lista muda de acordo com o   
    else: #val > lista[meio]:       #valor de meio
        ini = meio + 1

return -1 # quando o valor não existe na lista