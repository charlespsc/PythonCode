##########################################
### 4.6 Seção 6 - tuplas e dicionários ###
##########################################

### 4.6.1 Tipos de sequência e mutabilidade

### 4.6.2 Tuplas

# possível criar uma tupla apenas de um conjunto de valores separados por vírgulas.
# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, .125
 
# print(tuple_1)
# print(tuple_2)
 
# Como criar uma tupla

# empty_tuple = ()
 
# Se você deseja criar uma tupla de um elemento, precisa levar em consideração o fato de que, 
# devido a razões de sintaxe (uma tupla precisa ser distinguida de um valor único comum), 
# você deve terminar o valor com uma vírgula:
#
# one_element_tuple_1 = (1, )
# one_element_tuple_2 = 1.,

# Como usar uma tupla
# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)


# O que mais as tuplas podem fazer por você?
# - a função len() aceita tuplas e retorna o número de elementos contidos nela;
# - o operador + pode unir as tuplas (já mostramos isso)
# - o operador * pode multiplicar tuplas, assim como listas;
# - os operadores in e not in funcionam da mesma forma que nas listas.

# O fragmento no editor apresenta todos eles.
# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# Dê uma olhada no trecho de código:
# var = 123
 
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
 
# t1, t2, t3 = t2, t3, t1
 
# print(t1, t2, t3)
 
# Ele mostra três tuplas interagindo - com efeito, os valores armazenados nelas "circulam" - 
# t1 se torna t2, 
# t2 se torna t3 e 
# t3 se torna t1.

#########################
### 4.6.3 Dicionários ###
#########################

# Como fazer um dicionário
# Se você deseja atribuir alguns pares iniciais a um dicionário, use a seguinte sintaxe:

# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
# phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
 
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)

# print(dictionary['gato'])
# print(phone_numbers['Suzy'])


# O código a seguir pesquisa com segurança algumas palavras em francês:
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
# words = ['gato', 'lion', 'cavalo']
 
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "não está no dicionário")
 
# Quando você escreve uma expressão grande ou longa, pode ser uma boa ideia mantê-la alinhada verticalmente.
# É assim que você pode tornar seu código mais legível e mais fácil para programadores, por exemplo:
# # Exemplo 1:
# dictionary = {
#               "gato": "chat",
#               "cachorro": "chien",
#               "cavalo": "cheval"
# }
# # Exemplo 2:
# phone_numbers = {'chefe': 5551234567,
#               'Suzy': 22657854310
# }
 
# Esse tipo de formatação é chamado de recuo suspenso.


### 4.6.4 Métodos e funções de dicionário

## O método keys() 
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])
 
# Vamos agora dar uma olhada em um método de dicionário chamado items().
# O método retorna tuplas (este é o primeiro exemplo em que as tuplas são algo mais do que 
# apenas um exemplo delas) em que cada tupla é um par de valores-chave.

# Funciona assim:
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# for english, french in dictionary.items():
#     print(english, "->", french)
 
### Modificação e adição de valores

# Atribuir um novo valor a uma chave atual é simples - como os dicionários são totalmente mutáveis,
# não há obstáculos para modificá-los.

# Vamos substituir o valor "chat" por "minou", que não é muito preciso, mas funcionará bem com o nosso exemplo.

# Veja:
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# dictionary['gato'] = 'minou'
# print(dictionary)
 

# A função sorted()

# Deseja que ele seja ordenado? Basta enriquecer o loop for para obter o seguinte formulário:
# for key in sorted(dictionary.keys()):

# Há também um método chamado values(), que funciona de forma semelhante a keys(), mas retorna valores.

# Aqui está um exemplo simples:
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# for french in dictionary.values():
#     print(french)
 
# Adição de uma nova chave
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# dictionary['swan'] = 'cygne'
# print(dictionary)

# Você também pode inserir um item em um dicionário usando o método update(), por exemplo:
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# dictionary.update({"pato": "canard"})
# print(dictionary)
 

# Removendo uma chave
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# del dictionary['cachorro']
# print(dictionary)
 
# Para remover o último item de um dicionário, você pode usar o método popitem():
# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
# dictionary.popitem()
# print(dictionary)    # saídas: {'gato': 'chat', 'cachorro': 'chien'}
 
# Nas versões mais antigas do Python, ou seja, antes da versão 3.6.7, 
# o método popitem() remove um item aleatório de um dicionário.

#########################################################
### 4.6.5 Tuplas e dicionários podem trabalhar juntos ###
#########################################################
# 
#  
