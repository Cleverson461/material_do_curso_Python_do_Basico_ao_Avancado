""" 
    1 - Crie um programa que encontre e imprima as raizes de uma equação do segundo grau, utilizando o método de Bhaskara. 
    
"""

# 1 
# Equação do segundo grau: A * x ** 2 + B * x + C
# Coeficientes da equação quadrática ax² + bx + c = 0
a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = (b ** 2) - (4 * a * c) # Encontrando o valor de delta

x1 = (-b + delta ** 0.5) / (2 * a) # Encontrando as raizes x1 e x2
x2 = (-b - delta ** 0.5) / (2 * a)

# Na matemática, a raiz quadrada de um numero é igual a este numero elevado à meio (0.5)

print(f'As raízes são: {x1} e {x2}')


# outro modo de ser realizada a potência é utilizando o módulo math:

import math

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f'As raízes são: {x1} e {x2}')