
#######################################################
#### 3.7 Seção 7 - Listas em aplicativos avançados ####
#######################################################

### 3.7.1 Listas em listas ###
##############################

# row = [] 
# for i in range(8):
#     row.append(WHITE_PAWN)

##

# row = [WHITE_PAWN for i in range(8)]

# Veja outros exemplos de compreensão da lista:

# Exemplo #1:
# squares = [x ** 2 for x in range(10)]
# print(squares)
# # O snippet produz uma lista de dez elementos preenchida com quadrados de dez números inteiros começando em zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)


# # Exemplo #2:
# twos = [2 ** i for i in range(8)]
# print(twos)
# # O fragmento cria uma matriz de oito elementos que contém as oito primeiras potências de dois (1, 2, 4, 8, 16, 32, 64, 128)


# # Exemplo #3:
# odds = [x for x in squares if x % 2 != 0 ]
# print(odds) 
# # O fragmento faz uma lista com apenas os elementos ímpares da lista de squares.


### 3.7.2 Matrizes bidimensionais ###
#####################################

# Vamos supor também que um símbolo predefinido chamado EMPTY designa um campo vazio no tabuleiro.

# board = []
 
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# board = [[EMPTY for i in range(8)] for j in range(8)]

# Olhando de relance para a figura mostrada acima, vamos colocar algumas peças de xadrez no tabuleiro. Primeiro, vamos adicionar todas as gralhas:
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
 
# Se você quiser adicionar um Cavaleiro a C4, faça o seguinte:
# board[4][2] = KNIGHT
 
# E agora um peão para o E5:
# board[3][4] = PAWN
 
# 3.7.3 Natureza multidimensional das listas: aplicações avançadas
# Vamos aprofundar a natureza multidimensional das listas. Para encontrar qualquer elemento de uma lista bidimensional, você precisa usar duas coordenadas:

# a vertical (número da linha)
# e horizontal (número da coluna).

# Agora é hora de determinar a temperatura média mensal ao meio-dia. Adicione todas as 31 leituras gravadas ao meio-dia e divida a soma por 31. Você pode supor que a temperatura da meia-noite é armazenada primeiro. Aqui está o código relevante:


# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # A matriz é magicamente atualizada aqui.
# #
 
# total = 0.0
 
# for day in temps:
#     total += day[11]
 
# average = total / 31
 
# print("Temperatura média ao meio-dia:", average)
 
# Agora, encontre a temperatura mais alta durante todo o mês - veja o código:


# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # A matriz é magicamente atualizada aqui.
# #
 
# highest = -100.0
 
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
 
# print("A maior temperatura foi:", highest)

# Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:


# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # A matriz é magicamente atualizada aqui.
# #
 
# hot_days = 0
 
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
 
# print(hot_days, "dias estavam quentes.")



# O Python não limita a profundidade da inclusão na lista. Aqui você pode ver um exemplo de uma matriz tridimensional:

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
 
# Imagine um hotel. É um grande hotel composto de três edifícios, de 15 andares cada. Há 20 salas em cada andar. Para isso, você precisa de uma matriz que possa coletar e processar informações sobre as salas ocupadas/livres.

# Primeira etapa - o tipo dos elementos da matriz. Nesse caso, um valor booleano (True/False) seria adequado.
# Etapa dois - Análise calma da situação. Resuma as informações disponíveis: três edifícios, 15 andares, 20 salas.

# Agora você pode criar a matriz:

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# O primeiro índice (0 a 2) seleciona um dos edifícios; o segundo (0 a 14) seleciona o piso, o terceiro (0 a 19) seleciona o número do quarto. 
# Todas as salas são gratuitas.



# Agora você pode reservar um quarto para dois noivos: no segundo edifício, no décimo andar, quarto 14:
# rooms[1][9][13] = True
 
# e liberar a segunda sala no quinto andar, localizada no primeiro edifício:
# rooms[0][4][1] = False
 
# Verifique se há vagas no 15º andar do terceiro edifício:
# vacancy = 0
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1
 
# A variável vacancy contém 0 se todas as salas estiverem ocupadas ou o número de salas disponíveis em contrário.

# Parabéns! Você chegou ao final do módulo. Continue assim!



#############################
### 3.7.4 RESUMO DA SEÇÃO ###
#############################

# 1. A compreensão da lista permite criar novas listas a partir das existentes de forma concisa e elegante. 
# A sintaxe de uma compreensão de lista tem a seguinte aparência:

# [expressão para elemento na lista se condicional]
 
# que é equivalente ao seguinte código:

# for element in list:
#     if conditional:
#         expression
 
# Aqui está um exemplo de compreensão de lista - o código cria uma lista de cinco elementos preenchida com os cinco primeiros números naturais elevados à potência de 3:

# cubed = [num ** 3 for num in range(5)]
# print(cubed) # outputs: [0, 1, 8, 27, 64]
 

# 2. Você pode usar listas aninhadas em Python para criar matrizes (ou seja, listas bidimensionais). Por exemplo:

# # Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)
 
# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]
 
# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'
 

# 3. Você pode aninhar quantas listas desejar, criando assim listas n-dimensionais, por exemplo, matrizes de três, quatro ou até mesmo sessenta e quatro dimensões. 
# Por exemplo:

# # Cubo - uma matriz tridimensional (3x3x3)
 
# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],
 
#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],
 
#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]
 
# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'
 
# Pergunta 1
# Um operador capaz de verificar se dois valores são iguais é codificado como: ==

# Pergunta 2
# O valor eventualmente atribuído a x é igual a:
# x = 1
# x = x == x
# print(x)

# Pergunta 3
# Quantas estrelas (*) serão mandadas ao console pelo seguinte trecho de código?
# # i = 0
# while i <= 3 :
#     i += 2
#     print("*")
    
# Pergunta 4
# Quantas estrelas (*) serão mandadas ao console pelo seguinte trecho de código?
# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")

# Pergunta 5
# Quantos hashes (#) o snippet a seguir enviará para o console?
# for i in range(1):
#     print("#")
# else:
#     print("#")
    
# Pergunta 6
# Quantos hashes (#) o snippet a seguir enviará para o console?
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# Pergunta 7
# Quantos hashes (#) o snippet a seguir enviará para o console?
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
    
# Pergunta 8
# Que valor será atribuído à variável x?
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# Pergunta 9
# Qual é a saída do seguinte snippet?
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
 
# print(c + d + e)

# Pergunta 10
# Qual é a saída do seguinte snippet?
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])


# Pergunta 11
# Qual é a saída do seguinte snippet?
# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])


# Pergunta 12
# A segunda tarefa:
# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# # Reduz a lista

# Pergunta 13
# Após a execução do seguinte código, a soma de todos os elementos de vals será igual a:

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print (len(vals))

# Pergunta 14
# Dê uma olhada no snippet e escolha as afirmações verdadeiras: (selecione duas respostas)

# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]

# Pergunta 16
# Qual é a saída do seguinte snippet?

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)


# Pergunta 17
# Qual é a saída do seguinte snippet?

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)


# Pergunta 18
# Quantos elementos a lista my_list contém?

# my_list = [i for i in range(-1, 2)]
# print(len(my_list))

# Pergunta 19
# Qual é a saída do seguinte snippet?

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# Pergunta 20
# Qual é a saída do seguinte snippet?

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])
