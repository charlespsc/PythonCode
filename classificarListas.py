# 3.5 Seção 5 - Classificação de listas simples: o algoritmo de classificação bubblesort

# 3.5.1 A ordenção em bolhas

# 3.5.2 Ordenando uma lista

# my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
 
# for i in range(len(my_list) - 1):  # precisamos de (5 - 1) comparações
#     if my_list[i] > my_list[i + 1]:  # comparar elementos adjacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Se acabarmos aqui, nós temos que trocar os elementos.
# print(my_list) # Essa lista não ordena corretamente


# A lista será ordenada por bolhas com uma variável chamada swapped
#
# my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
# swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
# while swapped:
#     swapped = False  # nenhuma troca até agora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # uma troca ocorreu!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
# print(my_list)

#A ordenação por bolhas - versão interativa
# my_list = []
# swapped = True
# num = int(input("Quantos elementos você deseja embaralhar? "))

# for i in range(num):
#  val = float(input("Entre com a lista de elementos:"))
#  my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:", my_list)
#print(my_list) # tanto faz onde colocar a lista, mas com listas grandes faz mais sentido...

# Python, no entanto, tem seus próprios mecanismos de classificação.
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)

#############################
### 3.5.4 RESUMO DA SEÇÃO ###
#############################

# # 1. Você pode usar o método sort() para classificar elementos de uma lista, por exemplo:

# lst = [5, 3, 1, 2, 4]
# print(lst)
 
# lst.sort()
# print(lst)  # outputs: [1, 2, 3, 4, 5]
 
# #2. Há também um método de lista chamado revers(), que você pode usar para reverter a lista, por exemplo:

# lst = [5, 3, 1, 2, 4]
# print(lst)
 
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5]
  
  
  
 
############################
### 3.5.5 TESTE DA SEÇÃO ###
############################

#Pergunta 1: Qual é a saída do trecho de código?

# lst = ["D", "F", "A", "Z"]
# lst.sort()
 
# print(lst)


# #Pergunta 2: Qual é a saída do trecho de código?

# a = 3
# b = 1
# c = 2
 
# lst = [a, c, b]
# lst.sort()
 
# print(lst)

# #Pergunta 3: Qual é a saída do trecho de código?

# a = "A"
# b = "B"
# c = "C"
# d = " "
 
# lst = [a, b, c, d]
# lst.reverse()
 
# print(lst)


#########################################
### 3.6 Seção 6 - Operações em listas ###
#########################################

# 3.6.1 A vida interior das listas

# list_1 = [1]
# list_2 = list_1
# list_1 [0] = 2
# print(list_2)


# # 3.6.2 Os poderes do fatiamento

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# # my_list[start:end]
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# Copiar a lista inteira.
# list_1 = [1]
# list_2 = list_1 [:]
# list_1 [0] = 2
# print (list_2)

# # Copiando parte da lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list [1: 3]
# print(new_list)

#  3.6.3 Fatias - índices negativos

# my_list[start:end]

# É assim que os índices negativos trabalham com o particionamento:
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# Se o start especificar um elemento além do descrito no end (do início da lista), a fatia estará vazia:
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# print(new_list)

# # Se você omitir o start na fatia, presume-se que você deseja obter uma fatia começando no elemento com índice 0.
# my_list[:end]

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:3]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[3:]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list)

# Mais sobre a instrução del
# A instrução del descrita anteriormente é capaz de excluir mais do que apenas os elementos de uma lista de uma só vez - ela também pode excluir fatias:
    

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)


# # Também é possível excluir todos os elementos de uma só vez:
# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list)

# # A remoção da fatia do código muda bastante de significado.

# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)
 
# A instrução del excluirá a lista em si, não seu conteúdo.


### 3.6.4 Os operadores in e not in ###


