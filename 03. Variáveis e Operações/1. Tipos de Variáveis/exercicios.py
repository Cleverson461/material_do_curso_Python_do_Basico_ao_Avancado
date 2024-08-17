""" Exercícios:
1) Relacione as colunas de acordo com o tipo da variável.
(1)Inteiros                                     (5) “Casa”
(2) Float                                       (3) 2 + 0j
(3) Complexo                                    (4) True 
(4) Booleano                                    (5) ‘123’ 
(5) String                                      (2) 1.2345
                                                (4) False
                                                (5) ‘’’2j’’’
                                                (3) 10 + 1j
                                                (1) 2
                                                (5) ‘Programando Ideias’
                                                
2) Faça um programa que receba o nome de um aluno e quanto ele tirou na 
prova de programação, depois imprima em apenas uma linha o nome no modo 
title() e quanto a pessoa tirou na prova. Ex: Ana Carolina tirou 8
Respostas:
""" 

nome = input('Digite o nome da/o aluno/a: ')
nota = int(input('Digite a nota desse aluno/a: '))

print(f'{nome.title()} tirou {nota}')