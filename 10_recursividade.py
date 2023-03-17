"""
RECURSIVIDADE
Trata-se de uma técnica  de programação pela qual uma função chama a si mesma, em uma condição diferente da inicial. O principal objetivo de uso da recursividade é diminuir a complexidade de algoritmos.
"""

#Calculo do fatorial, versão iterativa (não recursiva)
def fatorial_iter(num):
    #Não é possivel calcular o fatorial de numeros negativos
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossivel")

    res = 1

    #loop descendente de num até 1
    for x in range(num, 0, -1): res *= x

    return res

############################################################################################

def fatorial_rec(num):
    #Não é possivel calcular o fatorial de numeros negativos
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossivel")

    if num <= 1: return 1       #O fatorial de 0 e 1 é 1 
    else: return num * fatorial_rec(num - 1) # Chamada recursiva a função

###########################################################################################

#print('7! = ', fatorial_iter(7))
#print('0! = ', fatorial_iter(0))
#print('-6! = ', fatorial_iter(-6))

print('7! = ', fatorial_rec(100))
print('0! = ', fatorial_rec(150))
print('-6! = ', fatorial_rec(600))