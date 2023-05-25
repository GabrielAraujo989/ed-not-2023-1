from LIB.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Insere o primeiro elemento 
lista.insert(0, "Macarrão")
print(lista)

#Insere no fim
lista.insert(1, "Molho de tomate")
print(lista)

#Insere em uma posição intermediaria
lista.insert(1, "Oleo de soja")
print(lista)

#Insere no final usando metodo de atalho
lista.insert.back("Queijo ralado")

#insere no inicio usando método de atalho
lista.insert_front("Carne moida")

#Mais uma inserção em posição intermediaria
lista.insert(3, "Sal")
print(lista)
