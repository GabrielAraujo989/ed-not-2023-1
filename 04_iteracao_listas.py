#Lista
frutas = ["laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

#Para percorrer uma lista e exibir apenas seus elementos, 
# usamos for.. in, como ja vimos no arquivo 02
for f in frutas:
    print(f)

print("-" * 80)

# Se quisermos percorrer a lista em ordem inversa para exibir apenas seus elementos, podemos usar for..in combinado com reversed()
for f in reversed(frutas):
    print(f)
print("|o|" * 80)

#Agora, se precisarmos exibir, alem do elemento, tambem sua posição devemos usar range()
for pos in range(len(frutas)):
    print(f"A Fruta {frutas[pos]} está na posição {pos}.")

print("\o/" * 50)

#Percurso em ordem inversa usando range() com 3 parametros
# os -1 servem para dar a posição de inicio e fim para o range
for i in range(len(frutas) -1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição {i}.")

print("\o/" * 50)