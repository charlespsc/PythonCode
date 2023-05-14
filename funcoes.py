
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
    
# def message():
#     print("Entre um valor: ")
 
# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())


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

# Um parâmetro é na verdade uma variável, mas há dois fatores importantes que tornam os parâmetros diferentes e especiais:

# parâmetros existem apenas dentro de funções nas quais eles foram definidos, e o único lugar onde o parâmetro pode ser definido é um espaço entre um par de parênteses na declaração def;
# a atribuição de um valor ao parâmetro é feita no momento da chamada da função, especificando o argumento correspondente.
# def function(parameter):
#     ###
    
# Não se esqueça:

# parâmetros vivem em funções internas (este é o ambiente natural)
# argumentos existem fora das funções e são portadores de valores passados para os parâmetros correspondentes.

# Vamos agora melhorar o corpo da função:
# def message(number):
#     print("Digite um número:", number)

# Parece melhor, com certeza:
# def message(number):
#     print("Digite um número:", number)
 
# message(1)

# def message(number):
#     print("Digite um número:", number)
 
# number = 1234
# message(1)
# print(number)

# Uma situação como essa ativa um mecanismo chamado shadowing:
    
#     O parâmetro x oculta qualquer variável com o mesmo nome, mas ...
# ... somente dentro da função que define o parâmetro.
    
#     O parâmetro chamado number é uma entidade completamente diferente da variável chamada number.

# Vamos modificar a função - ela tem dois parâmetros agora:

# def message(what, number):
#     print("Entrar", what, "número", number)

# def message(what, number):
#     print("Entrar com ", what, "número", number)
 
# message("telefone: ", 11)
# message("preço: ", 5)
# message("número: ", "47 9999-1234")



### 4.2.2 Passagem de parâmetros posicionais ###
################################################

# def my_function(a, b, c):
#     print(a, b, c)
 
# my_function(1, 2, 3)


# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction("Skywalker", "Luke")
# introduction("Quick", "Jesse")
# introduction("Kent", "Clark")
 
 
### 4.2.3 Passagem de parametro por palavra-chave ###
#####################################################

# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")



### 4.2.4 Mistura de argumentos posicionais e de palavras-chave ###
###################################################################

# Há apenas uma regra inquebrável: você precisa colocar argumentos posicionais antes dos argumentos das palavras-chave.

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
    
# # adding(1, 2, 3)
 
# # adding(c = 1, a = 2, b = 3)

# adding(3, c = 1, b = 2)


### 4.2.5 Funções parametrizadas – mais detalhes ###
####################################################






