"""
    Função para calcular o Índice de Massa Corpórea
    de uma pessoa, dados o seu peso e sua altura
"""
def imc(peso, altura):
    # Peso dividido pela altura elevada ao quadrado
    return peso / altura ** 2  

resultado = imc(81, 1.72)

print("O IMC calculado é ", resultado)

###########################################################

from math import pi

"""
    Declaração de uma função para calcular a área de figuras
    geométricas planas
"""
def calcular_area(base, altura, tipo):
    if tipo == "R":     # Retângulo
        return base * altura
    elif tipo == "T":   # Triângulo
        return base * altura / 2
    elif tipo == "E":   # Elipse ou círculo
        return (base / 2) * (altura / 2) * pi
    else:
        return None

# Chamadas à função anteriormente declarada
print("Área retângulo 10x25: ", calcular_area(10, 25, "R"))
print("Área triângulo 12x7:", calcular_area(12, 7, "T"))
print("Área círculo 10x10:", calcular_area(10, 10, "E"))