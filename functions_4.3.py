###########################################################
### 4.3 Seção 3 - Retornando um resultado de uma função ###
###########################################################
### 4.3.1 Efeitos e resultados: a instrução return ###
######################################################

### return sem uma expressão
# Vamos considerar a seguinte função:

# def happy_new_year(wishes = True):
#     print("Três...")
#     print("Duas...")
#     print("Uma...")
#     if not wishes:
#         return
 
#     print("Feliz Ano Novo!")

# happy_new_year()
# ou happy_new_year(False)
# # Saída:
# Três...
# Duas...
# Uma...


### return com uma expressão 
# def function():
#     return expression
 
# def boring_function():
#     return 123
 
# x = boring_function()
 
# print("A aborrecimento_função retornou seu resultado. Isso é:", x)
# # output: A boring_function retornou seu resultado. Isso é: 123


# def boring_function():
#     print("'Modo de tédio' ON.")
#     return 123

# print("Esta lição é interessante!")
# boring_function()
# print("Essa aula é chata...")


#########################################
### 4.3.2 Algumas palavras sobre None ###
#########################################

# Existem apenas dois tipos de circunstâncias em que None pode ser usada com segurança:

# quando você a atribui a uma variável (ou a retorna como resultado de uma função)
# quando você a compara com uma variável para diagnosticar seu estado interno.

# value = None
# if value is None:
#     print("Desculpe, você não carrega nenhum valor")

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
    
# print(strange_function(2))
# print(strange_function(1))
# Saída:
# True
# None


####################################################
### 4.3.3 Efeitos e resultados: listas e funções ###
####################################################

# Há duas perguntas adicionais que devem ser respondidas aqui.

# A primeira é: uma lista pode ser enviada para uma função como argumento?
# Claro que sim! 

# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s
 
# print(list_sum([5, 4, 3, 2, 1]))
# # Saída: 15


# A segunda pergunta é: uma lista pode ser um resultado de função?
# Sim, claro! 

# def strange_list_fun(n):
#  strange_list = []
 
#  for i in range(0, n):
#     strange_list.insert(0, i)
 
#  return strange_list

# print(strange_list_fun(5))

