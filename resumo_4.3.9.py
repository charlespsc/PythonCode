#############################
### 4.3.9 RESUMO DA SEÇÃO ###
#############################

# 1. Você pode usar a palavra-chave return para informar uma função para retornar algum valor.
# A declaração de return sai da função, por exemplo:

# def multiply(a, b):
#     return a * b
 
# print(multiply(3, 4))    # saídas: 12
 
 
# def multiply(a, b):
#     return
 
# print(multiply(3, 4))    # saídas: None
 
# 2. O resultado de uma função pode ser facilmente atribuído a uma variável, por exemplo:
# def wishes():
#     return "Feliz aniversário!"
 
# w = wishes()
 
# print(w)    # saídas: Feliz aniversário!
 
# Veja a diferença de saída nos dois exemplos a seguir:
# # Exemplo 1
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"
 
# wishes()    # saídas: Meus desejos
 
 
# # Exemplo 2
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"
 
# print(wishes())
 
# # saídas: Meus desejos
# #          Feliz aniversário!
 

# 3. Você pode usar uma lista como argumento de função, por exemplo:
# def hi_everybody(my_list):
#     for name in my_list:
#         print("Oi,", name)
 
# hi_everybody(["Adão", "John", "Lucy"]) 
# # saídas: Oi, Adão
# #         Oi, John
# #         Oi, Lucy
#

# 4. Uma lista também pode ser um resultado de função, por exemplo:
# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list
 
# print(create_list(5))
# # saídas: [0, 1, 2, 3, 4]


#############################
### 4.3.10 TESTE DA SEÇÃO ###
#############################

# Pergunta 1: Qual é a saída do trecho de código?
# def hi():
#     return
#     print("Oi!")
 
# hi()
# Resposta: A saída é None. 
# A função hi() retorna sem imprimir nada, pois a linha print("Oi!") 
# nunca é executada devido ao return anterior.

# Pergunta 2: Qual é a saída do trecho de código?
# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False
 
# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))
# Resposta: A saída é:
# True
# False
# None

# Pergunta 3: Qual é a saída do trecho de código?
# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
 
# print(even_num_lst(11))
# Resposta: A saída é:
# [0, 2, 4, 6, 8, 10]

# Pergunta 4: Qual é a saída do trecho de código?
# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list
 
# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))
# Resposta: A saída é:
# [1, 4, 9, 16, 25]


 
