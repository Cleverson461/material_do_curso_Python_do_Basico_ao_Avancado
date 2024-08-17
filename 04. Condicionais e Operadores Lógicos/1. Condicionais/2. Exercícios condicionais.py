""" 
    1 - Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência).
    
    Peça a operação desejada e depois os dois numeros ao usuário.
"""
opcao_desejada = input('Digite a operação desejada: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potência \n\n')

num1 = float(input('Digite o primeiro número: ')) # Convertendo o numero para float
num2 = float(input('Digite o segundo número: ')) # Convertendo o numero para float

if opcao_desejada == '1':
    resultado1 = num1 + num2
    print(f'A soma entre {num1} + {num2} = {resultado1}')
elif opcao_desejada == '2':
    resultado2 = num1 - num2
    print(f'A subtração entre {num1} - {num2} = {resultado2}')
elif opcao_desejada == '3':
    resultado3 = num1 * num2
    print(f'A multiplicação entre {num1} * {num2} = {resultado3}')
elif opcao_desejada == '4':
    resultado4 = num1 // num2
    print(f'A divisão inteira entre {num1} // {num2} = {resultado4}')
elif opcao_desejada == '5':
    resultado4 = num1 ** num2
    print(f'A divisão inteira entre {num1} ** {num2} = {resultado4}')
else:
    print('Opção inválida. Tente novamente.')