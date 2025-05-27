#######################################
### 4.4 Seção 4 - Escopos em Python ###
#######################################

# Olhe para o código:

# def my_function():
#  print("Eu conheço aquela variável?", var)

# var = 1
# my_function()
# print(var)

# Saída:
# Eu conheço aquela variável? 1
# 1
### A resposta é: uma variável existente fora de uma função tem escopo dentro do corpo da função.

# Vamos fazer uma pequena alteração no código:
# def my_function():
#     var = 2
#     print("Eu conheço aquela variável?", var)
 
 
# var = 1
# my_function()
# print(var)
 
# Saída:
# Eu conheço aquela variável? 2
# 1
### A resposta é: uma variável existente fora de uma função não pode ser acessada dentro do corpo da função,
#    a menos que seja declarada como global.

# Podemos tornar a regra anterior mais precisa e adequada:

# Uma variável existente fora de uma função tem escopo dentro do corpo da função, 
# excluindo aquelas que definem uma variável com o mesmo nome.

# Também significa que o escopo de uma variável existente fora de uma função é suportado 
# apenas ao obter seu valor (leitura). 
# A atribuição de um valor força a criação da própria variável da função.

#######################################################
### 4.4.2 Funções e escopos: a palavra-chave global ###
#######################################################

# Há um método Python especial que pode estender o escopo de uma variável de uma forma que inclua 
# o corpo da função (mesmo se você quiser não apenas ler os valores, mas também modificá-los).

# Tal efeito é causado por uma palavra-chave chamada global:
# def my_function():
#  global var
#  var = 2
#  print("Eu conheço aquela variável?", var)


# var = 1
# my_function()
# print(var)

# Saída:
# Eu conheço aquela variável? 2
# 2

########################################################
### 4.4.3 Como a função interage com seus argumentos ###
########################################################

# O código no editor deve ensinar alguma coisa. Como você pode ver, a função altera o valor de seu parâmetro.
# A mudança afeta o argumento?

# def my_function(n):
#  print("Eu obtive", n)
#  n += 1
#  print("Eu tenho", n)


# var = 1
# my_function(var)
# print(var)
# # Saída:
# # Eu obtive 1
# # Eu tenho 2
# # 1

# A conclusão é óbvia - alterar o valor do parâmetro não se propaga fora da função (em qualquer caso, 
# não quando a variável é escalar, como no exemplo).


# Isso também significa que uma função recebe o valor do argumento, não o próprio argumento.
# Isso se aplica a escalares.

# Vale a pena verificar como ele funciona com listas (você se lembra das particularidades de atribuir 
# fatias de lista versus atribuir listas como um todo?).

# O exemplo a seguir esclarecerá a questão:
# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)
# # Saída:
# # Print #1: [2, 3]
# # Print #2: [2, 3]
# # Print #3: [0, 1]        
# # Print #4: [2, 3]
# # Print #5: [2, 3]
# A conclusão é que, ao passar uma lista como argumento, a função recebe uma referência a essa lista.


# Por fim, você pode ver a diferença no exemplo abaixo:
# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0]  # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# # Saída:
# # Print #1: [2, 3]
# # Print #2: [2, 3]
# # Print #3: [3]
# # Print #4: [3]
# # Print #5: [3]
# A conclusão é que, ao passar uma lista como argumento, a função recebe uma referência a essa lista.


#############################
### 4.4.4 RESUMO DA SEÇÃO ###
#############################

# 1. Uma variável que existe fora de uma função tem escopo dentro do corpo da função (exemplo 1), 
# a menos que a função defina uma variável com o mesmo nome (exemplo 2 e exemplo 3), por exemplo:

# Exemplo 1:
# var = 2
 
# def mult_by_var(x):
#     return x * var
 
# print(mult_by_var(7))    # saídas: 14

# Exemplo 2:
# def mult(x):
#     var = 5
#     return x * var
 
# print(mult(7))    # saídas: 35
 
# Exemplo 3:
# def mult(x):
#     var = 7
#     return x * var
 
# var = 3
# print(mult(7))    # saídas: 49
 

# 2. Uma variável que existe dentro de uma função tem escopo dentro do corpo da função (exemplo 4), 
# por exemplo:

# Exemplo 4:
# def adding(x):
#     var = 7
#     return x + var
 
 
# print(adding(4))    # saídas: 11
# print(var)    # NameError
 
# 3. Você pode usar a palavra-chave global seguida por um nome de variável para tornar 
# o escopo da variável global, por exemplo:
# var = 2
# print(var)    # saídas: 2
 
 
# def return_var():
#     global var
#     var = 5
#     return var
 
 
# print(return_var())    # saídas: 5
# print(var)    # saídas: 5
 

############################
### 4.4.5 TESTE DA SEÇÃO ###
############################

# Pergunta 1: Qual é a saída do trecho de código?
# def message():
#     alt = 1
#     print("Olá Mundo!")
 
# print(alt)
# Saída:
# NameError: name 'alt' is not defined

# Pergunta 2: Qual é a saída do trecho de código?
# a = 1
 
# def fun():
#     a = 2
#     print(a)
 
# fun()
# print(a)
# Saída:
# 2
# 1

# Pergunta 3: Qual é a saída do trecho de código?
# a = 1
 
# def fun():
#     global a
#     a = 2
#     print(a)
 
# fun()
# a = 3
# print(a)
# Saída:
# 2
# 3

# Pergunta 4: Qual é a saída do trecho de código?
a = 1
 
 
def fun():
    global a
    a = 2
    print(a)
 
 
a = 3
fun()
print(a)
 
# Saída:
# 2
# 2