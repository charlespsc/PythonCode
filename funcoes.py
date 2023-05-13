
#################################
### 4.1.4 Sua primeira função ###
#################################

# print("Entre um valor: ")
# a = int(input())

# print("Entre um valor: ")
# b = int(input())

# print("Entre um valor: ")
# c = int(input())

# FUNÇÃO -> define = def

# def function_name():
#     function_body

# Estamos prontos para definir nossa função de prompt. Vamos dar o nome de message - aqui está:

# def message():
#     print("Entre um valor: ")
    
# def message():
#     print("Entre um valor: ")
 
# print("Começamos aqui.")
# print("terminamos aqui.")

# Isso significa que o Python lê as definições da função e as lembra, mas não inicia nenhuma sem a sua permissão.

# Nós modificamos o código agora - inserimos a chamada da função entre as mensagens de início e fim:
# def message():
#     print("Entre um valor: ")
 
# print("Começamos aqui.")
# message()
# print("terminamos aqui.")


# Vamos retornar ao nosso exemplo principal e empregar a função para o trabalho certo, como aqui:
    
def message():
    print("Entre um valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())


#############################
### 4.1.6 RESUMO DA SEÇÃO ###
#############################

# 1. Uma função é um bloco de código que executa uma tarefa específica quando a função é chamada (chamada). 
# Você pode usar funções para tornar seu código reutilizável, melhor organizado e mais legível. As funções podem ter parâmetros e valores de retorno.

# 2. Há pelo menos quatro tipos básicos de funções no Python:

#     1 - incorporadas que são parte integrante do Python (como a função de print()). 
#             Você pode ver uma lista completa das funções integradas do Python em https://docs.python.org/3/library/functions.html.
#     2 - os que vêm de módulos pré-instalados (você aprenderá sobre eles no curso Fundamentos do Python 2)
#     3 - funções definidas pelo usuário que são escritas pelos usuários para os usuários - você pode escrever suas próprias funções e usá-las livremente no código,
#     4 - funções lambda (você aprenderá sobre elas no curso Fundamentos do Python 2.)


# 3. Você pode definir sua própria função usando a palavra-chave def e a seguinte sintaxe:

# def your_function(optional parameters):
#     # o corpo da função
 
# Você pode definir uma função que não aceita argumentos, por exemplo:


# def message(): # definindo uma função
#     print("Olá") # o corpo da função
 
# message() # chamando a função
 
# Você pode definir uma função que aceita argumentos, assim como a função de um parâmetro abaixo:


# def hello(name): # definindo uma função
#     print("Olá,", name) # o corpo da função
 
 
# name = input("Entre um valor: ")
 
# hello(name) # chamando a função

 

############################
### 4.1.7 TESTE DA SEÇÃO ###
############################


# Pergunta 1: A função input() é um exemplo de a:

# a) função definida pelo usuário

# b) função integrada

# Resposta: 
# b - é uma função embutida.


# Pergunta 2: O que acontece quando você tenta invocar uma função antes de defini-la? Exemplo:


# hi()
 
# def hi():
#     print("hi!")
 
# Resposta: 
# Uma exceção é lançada (o NameError exceção para ser mais preciso).


# Pergunta 3: O que acontecerá quando você executar o código abaixo?


# def hi():
#     print("hi")
 
# hi(5)
 
# Resposta:
# Uma exceção será lançada (o TypeError exceção para ser mais preciso) - o hi() função não leva nenhum argumento.


####################################
### 4.2.1 Funções parametrizadas ###
####################################

