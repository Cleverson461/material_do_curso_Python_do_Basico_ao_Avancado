""" 
    1 - Crie um sistema de cadastro e login de um site, utilizando um username e senha informados pelo usuário.
""" 

# 1
login = False
print('Bem-vindo(a) ao cadastro do site!')

usarname = input('Digite o nome do usuário: ')
senha = input('Digite a sua senha: ')

print('\n __________LOGIN_________')

if input('Usuário: ') == usarname and input('Senha: ') == senha: # Testando as duas condições com o 'and'
    print('Login efetuado com sucesso!')
    login = True

if login: # if login == True
    print(f'\nBem-vindo(a) {usarname}')
else:
    print('Login ou senha incorretos! Tente novamente!')
    
    
    
# Obs.: É possível desenvolver o teste de login de outros modos e utilizando outros operadores, por exemplo:

if not login: # Utilizando o 'not' e troncando os prints
    print('\nLogin ou senha incorretos! Tente novamente!')
else:
    print(f'\nBem-vindo(a) {usarname}')
    

# OBS.: Adicionei um 'not' antes do 'login' para negar a condição e tronca os prints. Isso pode ser útil caso você deseja mostrar uma mensagem diferente para o caso de login incorreto.

if login is True: # Utilizando o 'is'
    print(f'\nBem-vindo(a) {usarname}')
else:
    print('Login ou senha incorretos! Tente novamente!')

# OBS.: Adicionei 'is True' para verificar se 'login' é igual a True. Isso pode ser útil caso você deseja mostrar uma mensagem diferente para o caso de login incorreto.