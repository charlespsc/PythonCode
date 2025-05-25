############################################
### 4.1.1 Por que precisamos de funções? ###
############################################

# - código é repetido várias vezes no programa.
# - se um fragmento específico do código começar a aparecer em mais de um lugar, 
# considere a possibilidade de isolá-lo na forma de uma função
# - se o código for longo e complexo, considere dividi-lo em partes menores,


##########################   
### 4.1.2 Decomposição ###
##########################

# - decomposição é o processo de dividir um problema em partes menores e mais gerenciáveis.
# - problema grande e complexo que não pode ser atribuído a um único desenvolvedor, 
# - problema deve ser dividido entre vários desenvolvedores de forma a garantir uma cooperação eficiente e perfeita.


#####################################
### 4.1.3 De onde vêm as funções? ###
#####################################

# Em geral, as funções vêm de pelo menos três lugares:
# - funções que você escreve
# - funções dos módulos que você importa
# - funções que vêm com o Python (funções internas)


#################################
### 4.1.4 Sua primeira função ###
#################################

# print("Entre um valor: ")
# a = int(input())

# print("Entre um valor: ")
# b = int(input())

# print("Entre um valor: ")
# c = int(input())

# def message():
#     print("Entre um valor: ")

# def message():
#     print("Entre um valor: ")
 
# print("Começamos aqui.")
# print("terminamos aqui.")
 
# def message():
#     print("Entre um valor: ")
 
# print("Começamos aqui.")
# message()
# print("terminamos aqui.")


####################################
### 4.1.5 Como funções funcionam ###
####################################

# Há duas coisas muito importantes. Aqui está a primeira:

# Você não deve invocar uma função que não é conhecida no momento da invocação.

# Lembre - se o Python lê seu código de cima para baixo. 
# Ela não vai olhar para frente para encontrar uma função que você esqueceu de colocar no lugar certo 
# ("certo" significa "antes da invocação".)

# Inserimos um erro neste código - Vê a diferença?
# print("Começamos aqui.")
# message()
# print("terminamos aqui.")
 
# def message():
#     print("Entre um valor: ")
# output: NameError: name 'message' is not defined

# Você não deve ter uma função e uma variável com o mesmo nome.

# O trecho a seguir está errado:
# def message():
#     print("Entre um valor: ")
 
# message = 1
# message()  # output: TypeError: 'int' object is not callable

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

# Você pode definir uma função que não aceita argumentos, por exemplo:
# def message():    # definindo uma função
#     print("Olá")    # o corpo da função
 
# message()    # chamando a função
 
# # Você pode definir uma função que aceita argumentos, assim como a função de um parâmetro abaixo:
# def hello(name):    # definindo uma função
#     print("Olá,", name)    # o corpo da função
 
 
# name = input("Digite o seu nome: ")
 
# hello(name)    # chamando a função
 

############################
### 4.1.7 TESTE DA SEÇÃO ###
############################

### Pergunta 1: A função input() é um exemplo de a:

# a) função definida pelo usuário
# b) função integrada
# Resposta: b) função integrada

### Pergunta 2: O que acontece quando você tenta invocar uma função antes de defini-la? 
# Exemplo:
# hi()
 
# def hi():
#     print("hi!")
 
# Resposta: Você receberá um erro de nome (NameError), porque o Python não conhece a função no momento da invocação.

### Pergunta 3: O que acontecerá quando você executar o código abaixo?
# def hi():
#     print("hi")
 
# hi(5)
 
# Resposta: Você receberá um erro de tipo (TypeError), porque a função hi() não aceita argumentos, 
# mas você tentou passar um.


###################################################################
### 4.2 Seção 2 - Como as funções se comunicam com seu ambiente ###
###################################################################
### 4.2.1 Funções parametrizadas ###
####################################

# Não se esqueça:
# parâmetros vivem em funções internas (este é o ambiente natural)
# argumentos existem fora das funções e são portadores de valores passados para os parâmetros correspondentes.

# def message(what, number):
#     print("Entrar", what, "número", number)
 
# message("telefone", 11)
# message("preço", 5)
# message("número", "número")
 

################################################
### 4.2.2 Passagem de parâmetros posicionais ###
################################################

# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")
 
# Agora, imagine que a mesma função está sendo usada na Hungria. 
# Nesse caso, o código ficaria assim:
# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction("Skywalker", "Luke")
# introduction("Quick", "Jesse")
# introduction("Kent", "Clark")


#####################################################
### 4.2.3 Passagem de parametro por palavra-chave ###
#####################################################

# def introduction(first_name, last_name):
#     print("Olá meu nome é", first_name, last_name)
 
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")


###################################################################
### 4.2.4 Mistura de argumentos posicionais e de palavras-chave ###
###################################################################

# Você pode combinar os dois estilos, se quiser - há apenas uma regra inquebrável: 
# você precisa colocar argumentos posicionais antes dos argumentos das palavras-chave.

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
 
# adding(1, 2, 3)


####################################################
### 4.2.5 Funções parametrizadas – mais detalhes ###
####################################################

# def introduction(first_name, last_name="Smith"):
#      print("Olá meu nome é", first_name, last_name)
 
# introduction("Luke", "Skywalker")
# output: Olá meu nome é Luke Skywalker

# def introduction(first_name, last_name="Smith"):
#     print("Olá meu nome é", first_name, last_name)

# introduction("Henry")
# output: Olá meu nome é Henry Smith

# Ambos os parâmetros têm seus valores padrão agora, veja o código abaixo:
# def introduction(first_name="John", last_name="Smith"):
#     print("Olá meu nome é", first_name, last_name)

# introduction()
# output: Olá meu nome é John Smith


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
 
# subtra(5, 2)    # saídas: 3
# subtra(2, 5)    # saídas: -3
 
 
# Ex. 2
# def subtra(a, b):
#     print(a - b)
 
# subtra(a=5, b=2)    # saídas: 3
# subtra(b=2, a=5)    # saídas: 3
 
# Ex. 3
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2)    # saídas: 3
# subtra(5, 2)    # saídas: 3
 
# É importante lembrar que argumentos de posição não devem seguir argumentos de palavra-chave. 
# É por isso que, se você tentar executar o seguinte trecho:
# def subtra(a, b):
#     print(a - b)
 
# subtra(5, b=2)    # saídas: 3
# subtra(a=5, 2)    # Syntax Error
 
# 3. Você pode usar a técnica de passagem de argumento da palavra-chave para predefinir um valor para um determinado argumento:
# def name(first_name, last_name="Smith"):
#     print(first_name, last_name)
 
# name("Andy")    # saídas: Andy Smith
# name("Betty", "Johnson")    # saídas: Betty Johnson (the keyword argument replaced by "Johnson")
 

############################
### 4.2.7 TESTE DA SEÇÃO ###
############################

# Pergunta 1: Qual é a saída do trecho de código?
# def intro(a="James Bond", b="Bond"):
#      print("Meu nome é", b + ".", a + ".")
 
# intro()
# # Resposta: Meu nome é Bond. James Bond.

# Pergunta 2: Qual é a saída do trecho de código?
# def intro(a="James Bond", b="Bond"):
#     print("Meu nome é", b + ".", a + ".")
 
# intro(b="Sean Connery")
# # Resposta: Meu nome é Sean Connery. James Bond.

# Pergunta 3: Qual é a saída do trecho de código?
# def intro(a, b="Bond"):
#     print("Meu nome é", b + ".", a + ".")
 
# intro("Susan")
# # Resposta: Meu nome é Bond. Susan.

# Pergunta 4: Qual é a saída do trecho de código?
# def add_numbers(a, b=2, c):
#     print(a + b + c)
 
# add_numbers(a=1, c=3)
# Resposta: SyntaxError: non-default argument follows default argument
# SyntaxError - um argumento não padrão (c) Segue um argumento default (b=2).


