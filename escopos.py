#########################################
#### 4.4 Seção 4 - Escopos em Python ####
#########################################

# 4.4.1 Funções e escopos

# def scope_test():
#  x = 123

# scope_test()
# print(x)
# Output -> NameError: name 'x' is not defined


# # Vamos começar verificando se uma variável criada fora de qualquer função é visível dentro das funções.
# def my_function():
#  print("Eu conheço aquela variável?", var)

# var = 1
# my_function()
# print(var)
# # A resposta é: uma variável existente fora de uma função tem escopo dentro do corpo da função.

# # Vamos fazer uma pequena alteração no código:
# def my_function():
#     var = 2
#     print("Eu conheço aquela variável?", var)
 
 
# var = 1
# my_function()
# print(var)
# # Output:
# # Eu conheço aquela variável? 2
# # 1


# 4.4.2 Funções e escopos: a palavra-chave global

# global name
# global name1, name2, ...

# Olhe para o código no editor.

# def my_function():
#  global var
#  var = 2
#  print("Eu conheço aquela variável?", var)


# var = 1
# my_function()
# print(var)

# Eu conheço aquela variável? 2
# 2

##########################################################
#### 4.4.3 Como a função interage com seus argumentos ####
##########################################################

def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)


var = 1
my_function(var)
print(var)
