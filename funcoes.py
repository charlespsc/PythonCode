
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


# def introduction(first_name, last_name="Smith"):
#      print("Olá meu nome é", first_name, last_name)

# introduction("Henry")
# ## output -> Olá meu nome é Henry Smith

# introduction("James", "Doe")
# ## output -> Olá meu nome é James Doe

# introduction(first_name="William")
# ## output -> Olá meu nome é

# def introduction(first_name="John", last_name="Smith"):
#     print("Olá meu nome é", first_name, last_name)
    
# introduction()
# introduction(last_name="Hopkins")

#############################
### 4.2.6 RESUMO DA SEÇÃO ###
#############################

# 1. Você pode passar informações para funções usando parâmetros. Suas funções podem ter quantos parâmetros forem necessários.

# Um exemplo de função de um parâmetro:


# def hi(name):
#     print("Oi,", name)
 
# hi("Greg")
 
# Um exemplo de função de dois parâmetros:


# def hi_all(name_1, name_2):
#     print("Oi,", name_2)
#     print("Oi,", name_1)
 
# hi_all("Sebastian", "Konrad")
 
# Um exemplo de função de três parâmetros:


# def address(street, city, postal_code):
#     print("Seu endereço é:", street, "St.,", city, postal_code)
 
# s = input("Street: ")
# p_c = input("Código postal: ")
# c = input("Cidade: ")
# address(s, c, p_c)
 
# 2. Você pode passar argumentos para uma função usando as seguintes técnicas:

# passagem de argumento posicional em que a ordem dos argumentos passou importa (Ex. 1)
# passagem de argumentos da palavra-chave (nomeada) na qual a ordem dos argumentos passados não importa (ex. 2)
# uma combinação de passagem de argumento de posição e de palavra-chave (por exemplo, 3.)

# Ex. 1
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, 2) # saídas: 3
# subtra(2, 5) # saídas: -3
 
 
# Ex. 2
# def subtra(a, b):
#     print(a - b)
 
# subtra(a=5, b=2) # saídas: 3
# subtra(b=2, a=5) # saídas: 3
 
# Ex. 3
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2) # saídas: 3
# subtra(5, 2) # saídas: 3
 
# É importante lembrar que argumentos de posição não devem seguir argumentos de palavra-chave. É por isso que, se você tentar executar o seguinte trecho:


# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2) # saídas: 3
# subtra(a=5, 2) # Syntax Error
 
# O Python não vai deixar e sinalizar um SyntaxError.

# 3. Você pode usar a técnica de passagem de argumento da palavra-chave para predefinir um valor para um determinado argumento:


# def name(first_name, last_name="Smith"):
#     print(first_name, last_name)
 
# name("Andy") # saídas: Andy Smith
# name("Betty", "Johnson") # saídas: Betty Johnson (the keyword argument replaced by "Johnson")
 
# Incompleta 4.2.7 TESTE DA SEÇÃO


############################
### 4.2.7 TESTE DA SEÇÃO ###
############################

# Pergunta 1: Qual é a saída do trecho de código?
# def intro(a="James Bond", b="Bond"):
#      print("Meu nome é", b + ".", a + ".")
 
# intro()
# Output -> Meu nome é Bond. James Bond.


# Pergunta 2: Qual é a saída do trecho de código?
# def intro(a="James Bond", b="Bond"):
#     print("Meu nome é", b + ".", a + ".")
 
# intro(b="Sean Connery")
# Output -> Meu nome é Sean Connery. James Bond.


# Pergunta 3: Qual é a saída do trecho de código?
# def intro(a, b="Bond"):
#     print("Meu nome é", b + ".", a + ".")
 
# intro("Susan")
# Output -> Meu nome é Bond. Susan.


# Pergunta 4: Qual é a saída do trecho de código?
# def add_numbers(a, b=2, c):
#     print(a + b + c)
 
# add_numbers(a=1, c=3)
# Output -> SyntaxError - um argumento não padrão (c) Segue um argumento default (b=2).


###########################################################
### 4.3 Seção 3 - Retornando um resultado de uma função ###
###########################################################

# Bem-vindo à seção 3! Nesta parte do curso, você aprenderá sobre os efeitos e resultados das funções, a expressão return e o valor None. 
# Você também aprenderá como passar listas como argumentos de função, como retornar listas como resultados de função e como atribuir resultados de função a variáveis. 

###  return sem uma expressão
#Vamos considerar a seguinte função:

# def happy_new_year(wishes = True):
#     print("Três...")
#     print("Duas...")
#     print("Uma...")
#     if not wishes:
#         return
 
#     print("Feliz Ano Novo!")
 
# # happy_new_year()
# happy_new_year(False)

###  return com uma expressão
#A segunda variante de return é estendida com uma expressão:

# def function():
#     return expression

# def boring_function():
#     return 123
 
# x = boring_function()
 
# print("A aborrecimento_função retornou seu resultado. Isso é:", x)


# Observe que não estamos sendo muito educados aqui - a função retorna um valor e nós o ignoramos (não o usamos de forma alguma):

# def boring_function():
#     print("'Modo de tédio' ON.")
#     return 123
 
# print("Esta lição é interessante!")
# boring_function()
# print("Essa aula é chata...")


#### 4.3.2 Algumas palavras sobre None ####
###########################################

# print(None + 2)

# value = None
# if value is None:
#     print("Desculpe, você não carrega nenhum valor")

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
    
# print(strange_function(2))
# print(strange_function(1))

### 4.3.3 Efeitos e resultados: listas e funções ###
####################################################

## Uma lista pode ser enviada para uma função como argumento?
## Uma função como esta aqui:

# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s
 
## e invocados da seguinte forma:
# print(list_sum([5, 4, 3]))

## Uma lista pode ser um resultado de função?
# Veja o código no editor:
    
# def strange_list_fun(n):
#  strange_list = []
 
#  for i in range(0, n):
#     strange_list.insert(0, i)
 
#  return strange_list

# print(strange_list_fun(5))




###############################
#### 4.3.9 RESUMO DA SEÇÃO ####
###############################

# 1. Você pode usar a palavra-chave return para informar uma função para retornar algum valor. A declaração de return sai da função, por exemplo:

# def multiply(a, b):
#     return a * b
 
# print(multiply(3, 4)) # saídas: 12
 
 
# def multiply(a, b):
#     return
 
# print(multiply(3, 4)) # saídas: None
 
 
# 2. O resultado de uma função pode ser facilmente atribuído a uma variável, por exemplo:

# def wishes():
#     return "Feliz aniversário!"
 
# w = wishes()
 
# print(w) # saídas: Feliz aniversário!
 
# # Veja a diferença de saída nos dois exemplos a seguir:

# # # Exemplo 1
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"
 
# wishes() # saídas: Meus desejos
 
# # Exemplo 2
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"
 
# print(wishes())
# # saídas: Meus desejos
# # Feliz aniversário!
 
 
# # 3. Você pode usar uma lista como argumento de função, por exemplo:

# def hi_everybody(my_list):
#    for name in my_list:
#    "woda": "água",
#          print("Oi,", name)
 
# hi_everybody(["Adão", "John", "Lucy"])
 
# # 4. Uma lista também pode ser um resultado de função, por exemplo:


# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list
 
# print(create_list(5))
 
 
############################### 
#### 4.3.10 TESTE DA SEÇÃO ####
###############################

# # Pergunta 1: Qual é a saída do trecho de código?

# def hi():
#     return
#     print("Oi!")
 
# hi()

# # Output -> A função retorna um valor implícito None.


# # Pergunta 2: Qual é a saída do trecho de código?

# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
 
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))

# # Output -> True, False, None


# # Pergunta 3: Qual é a saída do trecho de código?

# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
 
# print(even_num_lst(11))

# # Output -> [0, 2, 4, 6, 8, 10]


# # Pergunta 4: Qual é a saída do trecho de código?

# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list
 
# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))

# # Output -> [1, 4, 9, 16, 25]
