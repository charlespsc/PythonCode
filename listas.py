# # 3.4.1 Por que precisamos de listas?
# #
# numbers = [10, 5, 7, 2, 1]

# print("Terceira posição da lista: [10, 5, 7, 2, 1] -> ",numbers[2])


# # 3.4.2 Indexando listas
# numbers = [10, 5, 7, 2, 1]
# print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
# numbers[0] = 111
# print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista.
 
# numbers = [10, 5, 7, 2, 1]
# print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
# numbers[0] = 111
# print("\nConteúdo da lista anterior:", numbers)  # Imprimindo conteúdos de listas anteriores.
 
# numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
# print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.


# # 3.4.3 Acesso ao conteúdo da lista
# numbers = [10, 5, 7, 2, 1]
# print("Conteúdo da lista original:", numbers) # Imprimindo o conteúdo da lista original.


# numbers[0] = 111

# print ("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.


# numbers[1] = numbers [4] # Copiando o valor do quinto elemento para o segundo.
# print("Conteúdo da lista anterior:", numbers) # Imprimir o conteúdo da lista anterior.

# # A função len()

# print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista.


# # 3.4.4 Remover elementos de uma lista
# numbers = [10, 5, 7, 2, 1]

# del numbers[1]
# print(len(numbers))
# print(numbers)
 
# numbers = [10, 5, 7, 2, 1]
# print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.

# numbers[0] = 111
# print("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

# numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
# print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

# print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.

# ###

# del numbers[1] # Removendo o segundo elemento da lista.
# print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
# print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.

# numbers = [111, 7, 2, 1]
# print(numbers[-3])

# hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

#  # Etapa 1: escreva uma linha de código que solicita ao usuário
# # que substitua o número do meio por um número inteiro inserido pelo usuário. 
# hat_list[-3] = 111


# # Etapa 2: escreva uma linha de código que remova o último elemento da lista.
# del hat_list[-1]

#  # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual
# len (hat_list)

# print (hat_list) 
# print (len (hat_list)) 


# 3.4.7 Funções x métodos

# 3.4.8 Adicionando elementos a uma lista: append() e insert()

# numbers = [111, 7, 2, 1]

# print(len(numbers))

# print(numbers)


#  ###


# numbers.append (4)


# print(len(numbers))

# print(numbers)

# ###

# numbers.insert (0, 222)

# print(len (numbers))
# print(numbers)

# numbers.insert(1, 333)
# print(len (numbers))
# print(numbers)
 

# my_list = [] # Criando uma lista vazia.

# for i in range(5):
#    my_list.append (i + 1)

# print (my_list)


# my_list = []  # Criando uma lista vazia.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
 
# print(my_list)
 
# # 3.4.9 Utilização de listas

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#   total += my_list[i]
# print(total)

# my_list = [10, 1, 8, 3, 5]
# total = 0
 
# for i in my_list:
#     total += i
# print(total)
 

# 3.4.10 Listas em ação
# Pergunta: como você pode trocar os valores de duas variáveis?
# O Python oferece uma maneira mais conveniente de fazer a troca - dê uma olhada:
# variable_1 = 1
# variable_2 = 2
 
# variable_1, variable_2 = variable_2, variable_1
 
# print(variable_1)
# print(variable_2)

# my_list = [10, 1, 8, 3, 5]
 
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)
 
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)
 
