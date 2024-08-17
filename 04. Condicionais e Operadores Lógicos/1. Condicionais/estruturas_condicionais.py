""" 
    Estruturas condicionais
    
    if(se), elif(senão se), else(senão)
    
-----------------------------------------------------------   
# Testar altura para brinquedo do parque #
altura = float(input('Digite sua altura: '))

if altura < 1.6:
    print('Você não pode brincar no parque.')
else:
    print('Você pode brincar!')
    
------------------------------------------------------------
# Consultar média final para aprovação
nota = float(input('Digite a sua nota: '))

if nota > 6:
    print('Você foi aprovado! Pode curtir suas férias')
elif nota == 6:
    print('Pode curtir suas férias.')
else:
    print('Você não foi aprovado. Te vejo ano que vem outra vez.')
    
if nota >= 6:
    print('Você passou, pode curtir suas férias')
else:
    print('Você não passou. Se desejar, pode tentar novamente.')

------------------------------------------------------------------
# Determinar se um número é par ou impar
num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O {num} é par.')
else:
    print(f'O {num} é impar.')
    
if num % 2 != 0:
    print(f'O {num} é impar.')
else:
    print(f'O {num} é par.')

------------------------------------------------------------
# utilizando outros tipos de dados
# Strings
pais = input('Digite um pais que voce deseja visitar: ')

if pais == 'Noruega':
    print('Ah nao, muito frio!')
elif pais == 'China':
    print('Ah, China é um lugar muito longe!')
elif pais == 'Autrália':
    print('Ah, aqui é um lugar muito canguru!')
else: 
    print('Vamos.')

-----------------------------------------------------------
# utilizando outros tipos de dados
# Boolean

login = False
senha = '1234'

key = input('Digite sua senha: ')

if key == senha:
    login = True
else:
    print('Senha incorreta!')
    
if login == True:
    print('Bem-vindo admin - Login efetuado com sucesso!')
else:
    print('Tente novamente!')
"""

# Cuidado com as variaveis locais e globais

login = False # Variável global
senha = '1234'
key = '1234'

if key == senha:
    login = True # Variável local
else:
    print('Senha incorreta!')

# if login == True:
if login:
    print('Bem-vindo admin - Login efetuado com sucesso!')
else:
    print('Tente novamente!')
    
""" 
# Lista de operadores

>  - maior
<  - menor
>= - maior ou igual
<= - menor ou igual
== - igual
!= - diferente
%  - resto

"""