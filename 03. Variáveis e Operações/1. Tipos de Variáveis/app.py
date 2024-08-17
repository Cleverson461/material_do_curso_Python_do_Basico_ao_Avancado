# ** Variaveis e Tipos de Dados **

""" 
    O que são Variaveis?
      - São um modo de rotular ou nomear todos os dados pertencentes ao seu programa.
      - Variaveis são nomes que podem ser usados para armazenar valores.
      
    O que são Dados?
    - São todas as informações que serão utilizadas ao longo do seu código. Podendo ser números, palavras, frases, textos, dentre outros.
    - São os valores que são armazenados em variaveis. 
    
    Existem 2 Tipos de variaveis:
        1) Variavel Global: São variaveis que podem ser manipuladas ao longo de todo código.
        2) Variavel Local: São variaveis que podem ser manipuladas apenas em uma determinada parte do programa. 
                        - São variaveis que podem ser manipuladas apenas dentro de um bloco de código (funcao, loop, etc.).
                      
    Como declarar variaveis?
    nome = dado
    
    É necessario algumas regras para nomear sua variaveis:
    a) Em nomes compostos devemos separar por underline ou letra maiusculas.
    Ex:
        - Modo Certo (Pytonico):
            idadeJoao = 13
            idade_joao = 13
            IDADE_JOAO = 13
        
        - Modo Errado (Nao Pytonico):
            idadejoao = 13
            
    b) Variaveis não devem possuir nenhum tipo de caracter especial (%, acentos, ç, dentre outros).
    Ex:
        - Modo Certo:
            fracao = 100
            
        - Modo Errado:
            fração = 100
    
    c) Variaveis não devem possuir apenas numeros em seu nome. 
    Ex:
        - Modo Errado:
            123 = 17 # Irá acusar erro
        - Modo Certo:
            valor123 = 17 # Irá funcionar corretamente
        OBS: Ao utilizar numeros na nomeclatura de variaveis devem sempre vir no minimo uma letra antes dos numeros.
        
        
Tipos de Dados:
a) Inteiros: Número que não possui casas decimais.
Ex:
idadeJoao = 17
print(type(idadeJoao)) # Para utilizar a função type faça: type(nome da variavel).

b) Flutuantes (float): Números que possuem casas decimais.
   - Utiliza-se ponto para separar os números, NÃO VÍRGULA.
   - Não utiliza espaços em volta do ponto. 
   - Apresenta maior precisão e riqueza de dados.
Ex:
precoBanana = 5.59
print(type(precoBanana))

C) Complexo: - Se um dado possuir a letra j é um numero complexo, lembrando que precisa de haver um numero junto a ele. 
Ex:
numeroCompleto = 2 - 2j
print(numeroCompleto)
print(type(numeroCompleto))

D) Booleana: - O valor 1 representa True (Verdadeiro), enquanto o valor 0 representa False (Falso).
Ex:
var_bool = True
print(var_bool)
print(type(var_bool))

E) String: - Todos os dados que estão entre aspas simples, aspas duplas ou aspas simples triplas.
           - Podem conter numeros e letras dentro dela.
           - Para inverter o conteudo presente na string basta adicionar [::-1]
Ex:
var_string = 'Tom cruise'
print(var_string)
print(type(var_string))

print("===================================")

var_string = "Tom cruise"
print(var_string)
print(type(var_string))

print("===================================")

var_string = '''Tom cruise'''
print(var_string)
print(type(var_string))

var_string = 'Tom cruise'
print(var_string[::-1])
print(type(var_string))

var_string = "Tom cruise"
print(var_string[4:10]) # Estou pegando a posição 4(c) até a posição 9(e)
print("===================================")
var_String = 'turquia god of war'
print(var_String[6:13]) # Estou pegando a posição 6(a) até o posição 12(o)

Por fim, é possivel declarar varias variaveis dentro de uma mesma linha.
Ex:
a1, a2, a3, a4, a5= 1, 2.5, True, 2j, "Tom cruise"
    - Caso haja mais dados ou variaveis em algum dos lados irá dar erro.
"""

a1, a2, a3, a4, a5= 1, 2.5, True, 2j, "Tom cruise"

print(f'a1: {a1}, tipo: {type(a1)}')
print(f'a2: {a2}, tipo: {type(a2)}')
print(f'a3: {a3}, tipo: {type(a3)}')
print(f'a4: {a4}, tipo: {type(a4)}')
print(f'a5: {a5}, tipo: {type(a5)}')