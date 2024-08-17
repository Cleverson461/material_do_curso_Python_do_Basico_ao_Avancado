# Exercicios
## 1) Descubra quais erros estão presentes nos códigos abaixo:
""" nome = 'Mark'
print(int(nome)) # Não é possível transformar letras em inteiros
# ValueError: invalid literal for int() with base 10: 'Mark' """

# filme = 'Avatar'
# print('A maior bilheteria de 2009 foi {filme}') # Falta acrescentar a letra f antes do primeiro aspas

"""frase = 'Eu sou seu pai'
print(frase[-1::]) # Sintaxe incorreta.
print(frase[:: -1]) # o certo é utilizar [::-1]
"""

""" numero1 = 10
dado = int(input(Digite o numero que deseja: )) # Faltou o uso de aspas em volta do texto em input()
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(numero1 * dado) """

## 2) Criação de personagem de mundo de ficção, apresentando opções de acordo com os tipos das variáveis: 

""" 
    - Cor de Cabelo (string)
    - Cor de pele (string)
    - Classe: Guerreiro, Mago, Arqueiro (string)
    - Idade (int)
    - Altura (float)
    - Habilidade Especifica (string)
    
    Imprima para o usuario o personagem completo.
"""

print('---------- Bem Vindo a um novo Universo ---------- ')
print('-------------- Crie seu personagem ----------------')
nome_do_personagem_ficticio = input('Digite um nome de personagem: ')
cor_de_cabelo = input('Digite uma cor de cabelo: ')
cor_de_pele = input('Digite uma cor de pele: ')
classe_de_guerreiros = input('Escolha uma classe do personagem: 1 - Guerreiro\n2 - Mago\n3 - Arqueiro\nOpção: ')
idade = int(input('Digite uma idade: '))
altura = float(input('Digite uma altura: '))
habilidade_especifica = input('Digite uma Habilidade Especifica: ')

print('------------- Personagem Criado -------------------')

print(f'O nome do personagem é {nome_do_personagem_ficticio}\n a cor do cabelo é {cor_de_cabelo}\n sua cor de pele é {cor_de_pele}\n sua classe é {classe_de_guerreiros}\n tem idade {idade}\n anos com altura de {altura}\n e sua habilidade especifica é {habilidade_especifica} .')