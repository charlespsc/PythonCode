############################
### 3.4 Seção 4 - Listas ###
############################

# numbers = [10, 5, 7, 2, 1]
# print(numbers)


### 3.4.2 Indexando listas ###
##############################

# # numbers = [10, 5, 7, 2, 1]
# # print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
# # numbers[0] = 111
# # print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista.

# # numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
# # print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.


### 3.4.3 Acesso ao conteúdo da lista ###
#########################################

# print(numbers[0]) # Acessando o primeiro elemento da lista.

# numbers = [10, 5, 7, 2, 1]
# print("Conteúdo da lista original:", numbers) # Imprimindo o conteúdo da lista original.

# numbers[0] = 111

# print ("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

# numbers[1] = numbers [4] # Copiando o valor do quinto elemento para o segundo.
# print("Conteúdo da lista anterior:", numbers) # Imprimir o conteúdo da lista anterior.

# print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista.


### 3.4.4 Remover elementos de uma lista ###
############################################

# numbers = [10, 5, 7, 2, 1]
# print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.

# numbers[0] = 111
# print("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

# numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
# print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

# print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.

# ###############################################

# del numbers[1] # Removendo o segundo elemento da lista.
# print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
# print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.


### 3.4.5 Os índices negativos são legais ###
#############################################

# numbers = [111, 7, 2, 1]
# print(numbers[-4])
#
#
### 3.4.7 Funções x métodos ###
###############################

# 3.4.8 Adicionando elementos a uma lista: append() e insert()

# Ele pega o valor do argumento e o coloca no final da lista que possui o método.
# list.append(value)

# Ele pode adicionar um novo elemento em qualquer lugar na lista, não apenas no final.
# list.insert(location, value)


# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# ###

# numbers.append (4)
# print(len(numbers))
# print(numbers)

# ###

# numbers.insert (0, 222)
# print(len (numbers))
# print(numbers)

# numbers.insert(1, 333)
# print(len(numbers))
# print(numbers)

# ###

# Você pode começar a vida de uma lista deixando-a vazia (isso é feito com um par de colchetes vazios) e, em seguida, adicionando novos elementos, conforme necessário.

# my_list = [] # Criando uma lista vazia.

# for i in range(5):
#    my_list.append (i + 1)

# print (my_list)


# Modificamos um pouco o snippet:
    
# my_list = []  # Criando uma lista vazia.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
 
# print(my_list)

# Você deve obter a mesma sequência, mas em ordem inversa (este é o mérito de usar o método insert()).
#
#
### 3.4.9 Utilização de listas ###
##################################
#
# O código somou todos os itens da lista colocando dentro da variável total.
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in range(len(my_list)):
#   total += my_list[i]
# print(total)

# O segundo aspecto do loop for
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in my_list:
#     total += i
# print(total)


### 3.4.10 Listas em ação ###
#############################

# Pergunta: como você pode trocar os valores de duas variáveis?

# variable_1 = 1
# variable_2 = 2
 
# variable_2 = variable_1
# variable_1 = variable_2

# Se você fizer algo assim, você perderia o valor armazenado anteriormente na variável_2. 
# Alterar a ordem das tarefas não vai ajudar. 

# Você precisa de uma terceira variável que serve como armazenamento auxiliar.

# É assim que você pode fazer:

# variable_1 = 1
# variable_2 = 2
 
# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary


# O Python oferece uma maneira mais conveniente de fazer a troca - dê uma olhada:
#
# variable_1 = 1
# variable_2 = 2
 
# variable_1, variable_2 = variable_2, variable_1
 
# Agora você pode facilmente trocar os elementos da lista para reverter a ordem:

# my_list = [10, 1, 8, 3, 5]
 
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)

# Parece bom com cinco elementos.
# Ainda será aceitável com uma lista contendo 100 elementos? Não, não vai.

# Você pode usar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista? Sim, você pode.
# É assim que fizemos:

# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)
# -> AQUI tem algum problema que não dei o tempo devido para saber o que é...



##############################
### 3.4.12 RESUMO DA SEÇÃO ###
##############################

# 1. A lista é um tipo de dados em Python usado para armazenar vários objetos. É uma coleção ordenada e mutável de itens separados por vírgula entre colchetes, por exemplo:
# my_list = [1, None, True, "eu sou um barbante", 256, 0]


# 2. As listas podem ser indexadas e atualizadas, por exemplo:
# my_list = [1, None, True, 'eu sou um barbante', 256, 0]
# print(my_list[3])  # outputs: eu sou um barbante
# print(my_list[-1])  # outputs: 0
 
# my_list[1] = '?'
# print(my_list)  # outputs: [1, '?', True, 'eu sou um barbante', 256, 0]
 
# my_list.insert(0, "primeiro")
# my_list.append("último")
# print(my_list)  # outputs: ['primeiro', 1, '?', True, 'eu sou um barbante', 256, 0, 'último']
#
#
#3. As listas podem ser aninhadas, por exemplo:
# my_list = [1, 'a', ["lista", 64, [0, 1], False]]
 
# Você aprenderá mais sobre o aninhamento no módulo {{_globals._moduleNumber}}.7 - Por enquanto, queremos que você esteja ciente de que algo como isso também é possível.
 
# 4. Os elementos e as listas podem ser excluídos, por exemplo:
# my_list = [1, 2, 3, 4]
# del my_list[2]
# print(my_list)  # outputs: [1, 2, 4]
 
# del my_list  # exclui toda a lista


# 5. As listas podem ser iteradas usando o loop for, por exemplo:
# my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
 
# for color in my_list:
#     print(color)
 
 
# 6. A função len() pode ser usada para verificar o comprimento da lista, por exemplo:
# my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
# print(len(my_list))  # outputs 5
 
# del my_list[2]
# print(len(my_list))  # outputs 4

# 7. Uma chamada de função típica tem a seguinte aparência: result = function(arg), 
# enquanto uma chamada de método típico se parece com isso: result = data.method(arg).

#############################
### 3.4.13 TESTE DA SEÇÃO ###
#############################

# Pergunta 1: Qual é a saída do trecho de código?

# lst = [1, 2, 3, 4, 5]
# lst.insert(1, 6)
# del lst[0]
# lst.append(1)
 
# print(lst) # Output [6, 2, 3, 4, 5, 1]


# Pergunta 2: Qual é a saída do trecho de código?
# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0
 
# for number in lst:
#     add += number
#     lst_2.append(add)
 
# print(lst_2)


# Pergunta 3: Qual é a saída do trecho de código?
# lst = []
# del lst
# print(lst) # NameError: name 'lst' is not defined
 
 
# Pergunta 4: Qual é a saída do trecho de código?
# lst = [1, [2, 3], 4]
# print(lst[2])
# print(len(lst))



