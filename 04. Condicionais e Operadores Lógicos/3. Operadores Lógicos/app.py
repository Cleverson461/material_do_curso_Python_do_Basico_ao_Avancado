""" 
    Estruturas lógicas
    
    and(e), or(ou), not(não)
    
    - and(e): True apenas se todas as condições forem True
# and 
# Exemplo 1
sensor = 875 # range de segurança do sensor: 60 a 75

if sensor >= 60 and sensor <= 75:
    print('Tudo OK!')
else:
    print('Atenção! Corre! Alarme ativado!')
    
# Exemplo 2
agua = True
comida = True

if agua and comida:
    print('Cachorro feliz!')
else:
    print('Cachorro triste e mal humorado!')
    
====================================================================================
    - or(ou): True quando pelo menos uma condição for True - se alguma das condições forem True

# or
# Exemplo 1
pizza = False
lasanha = False

if pizza or lasanha:
    print('Preciso comer mais salada')
else:
    print('Estou com fome')
    
    
# Exemplo 2
num = 23

if num % 2 == 0 or num < 10:
    print(f'O {num} é par ou menor que 10')
else:
    print(f'O {num} é ímpar e maior ou igual a 10')
    
====================================================================================
    - is(é):  Comparação entre valores, similar ao ==
    
# is
# Exemplo 1
login = False
print(login is True) # Login é True? R: NÃO - (False)
print(login is False) # Login é False? R: SIM - (True)

if login is True:
    print('Bem-vindo admin - Login efetuado com sucesso!')
else:
    print('Tente novamente! Deslogado.')
====================================================================================
    - not(não): Inversão do valor booleano(True -> False, False -> True) == True se a condição for False e False se a condição for True
# not
# Exemplo 1
login = False

if not login: # não False: True
    print('Deslogado!')
else:
    print('Logado.')
"""


