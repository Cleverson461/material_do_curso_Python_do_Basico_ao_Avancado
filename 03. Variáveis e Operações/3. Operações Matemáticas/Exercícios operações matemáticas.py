""" 
1 - Realizar a média das notas de 4 alunos. 

2 - Converter uma temperatura de graus °C para ºF e para K.
Dados: ºF = ºC * 1.8 + 32, K = ºC + 273.15
"""

# nome = input('Nome do Aluno: ')
# n1 = int(input('Digite a primeira nota: '))
# n2 = int(input('Digite a segunda nota: '))
# n3 = int(input('Digite a terceira nota: '))
# n4 = int(input('Digite a quarta nota: '))
# media = (n1 + n2 + n3 + n4) / 4

# print(f'A média das notas de {nome} é {media}')

temperatura = float(input('Digite uma temperatura em graus Celsius: ')) 
F = temperatura * 1.8 + 32
K = temperatura + 273.15


print(f'{temperatura}°C equivalem a {F}°F')
print(f'{temperatura}°C equivalem a {K} Kelvin')
