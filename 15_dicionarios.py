pessoa = {
    "nome" : "Orozimbo Oliver Osório",
    "sexo" : "M" ,
    "idade" : 71 , 
    "peso" : 76 ,
    "altura" : 1.66 , 
    "aposentado" : True
}

#Acessando os valores armazenados no dicionario
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado? ", pessoa["aposentado"])

# Calcula o IMC da pessoa
imc = pessoa["peso"] / pessoa["altura"] ** 2
print(f"O IMC de {pessoa['nome']} é: {imc}.")

######################################################################

forma1 = {
    "base" : 6,
    "altura" : 2.5,
    "tipo" : "T"  #triangulo
}

forma2 = {
     "base" : 7.5,
    "altura" : 12,
    "tipo" : "R"  #retangulo
}

forma3 = {
     "base" : 5,
    "altura" : 3,
    "tipo" : "E"  #elipse
}

forma4 = {
    "base" : 11,
    "altura" : "batata",
    "tipo" : "T"
}

from math import pi

def calculadora_area(forma):
    if forma["tipo"] == "R":   #retangulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":   #triangulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":   #Elipse
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else:
        return None

##########################################################################################
#calculando a area das formas
print(f"Base: {forma1['base']}; altura: {forma1['altura']}; tipo: {forma1['tipo']}; ÁREA: {calculadora_area(forma1)}")

print(f"Base: {forma2['base']}; altura: {forma2['altura']}; tipo: {forma2['tipo']}; ÁREA: {calculadora_area(forma2)}")

print(f"Base: {forma3['base']}; altura: {forma3['altura']}; tipo: {forma3['tipo']}; ÁREA: {calculadora_area(forma3)}")

print(f"Base: {forma4['base']}; altura: {forma4['altura']}; tipo: {forma4['tipo']}; ÁREA: {calculadora_area(forma4)}")