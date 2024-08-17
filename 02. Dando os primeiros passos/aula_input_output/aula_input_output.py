"""  
Input e Output

Output - print(): Apresenta dados para o usuário

Input - input(): Recebe dados do usuário

#Obs.: Os dados recebidos são do tipo String.
"""

# print('Digite uma cor: ')

# cor = input()
# print(cor)

# Versões 2.x
# print('Você escolheu a cor %s' % cor)

# Versões 3.x até 3.7
# print('Você escolheu a cor {0}'.format(cor))

# Versões a partir da 3.7
# print(f'Voce escolheu a cor {cor}')
""" cor =input('Digite uma cor: ')
print(f'Voce escolheu a cor {cor}') """

# Print sem pular linha
""" print('Tomate')
print('Tomate')
print('Tomate')

print('tomate', end=' ')
print('tomate', end=' ')
print('tomate', end=' ') """

# cor = input('Digite uma cor: ')
# num = input('Digite um numero: ')

# print(f'Voce escolhe a cor {cor} e o numero {num}')

# Realizar operações nas saidas (print)
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
soma = int(num1 + num2)

print(f'A soma dos numeros {num1} e {num2} eh {soma}')

# Obs.: Casting - conversão de um tipo de dado para outra
