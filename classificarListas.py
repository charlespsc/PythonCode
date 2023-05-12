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


# my_list = [0, 3, 12, 8, 2]

# print(5 in my_list)             # False
# print(5 not in my_list)         # True
# print(12 in my_list)            # True


# 3.6.5 Listas - alguns programas simples

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list:
#     if i > largest:
#         largest = i
 
# print(largest)


# Se precisar economizar energia do computador, use uma fatia:

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
 
# print(largest)


# Agora vamos encontrar a localização de um determinado elemento dentro de uma lista:

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
 
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
 
# if found:
#     print("Elemento encontrado no índice", i)
# else:
#     print("ausente")
    
###########################
# 3.6.7 RESUMO DA SEÇÃO ###
###########################

# 1. Se você tiver uma lista list_1, a seguinte atribuição: list_2 = list_1 não faz uma cópia da lista list_1,
#           mas faz com que as variáveis list_1 e list_2 apontem para uma mesma lista na memória. Por exemplo:

vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one) # outputs: ['carro', 'bicicleta', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # exclui 'carro'
print(vehicles_two) # outputs: ['bicicleta', 'motor']

 
# 2. Se quiser copiar uma lista ou parte da lista, você pode fazer isso dividindo:

colors = ['vermelho', 'verde', 'laranja']
 
copy_whole_colors = colors[:]  # copie a lista inteira
copy_part_colors = colors[0:2]  # copiar parte da lista
 
 
# 3. Você também pode usar índices negativos para executar fatias. Por exemplo:

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
 
 
# 4. Os start de end e fim são opcionais ao executar uma fatia: list[start:end], por exemplo:

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
 
 
# 5. Você pode excluir fatias usando a instrução del:

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
 
del my_list[:]
print(my_list)  # deletes the list content, outputs: []
 
 
# 6. Você pode testar se alguns itens existem em uma lista ou não estão usando as palavras-chave in e not in, por exemplo:

my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
 
 
 
###############################
####  3.6.8 TESTE DA SEÇÃO ####
###############################

# Pergunta 1: Qual é a saída do trecho de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0]
 
print(list_3)


# Pergunta 2: Qual é a saída do trecho de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2
 
print(list_3)


# Pergunta 3: Qual é a saída do trecho de código?

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[:]
 
print(list_3)


# Pergunta 4: Qual é a saída do trecho de código?

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
 
del list_1[0]
del list_2[0]
 
print(list_3)


# Pergunta 5: Insira in ou not in ao invés de ??? para que o código produz o resultado esperado.

my_list = [1, 2, "in", True, "ABC"]
 
print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False