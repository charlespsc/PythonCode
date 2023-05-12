
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
squares = [x ** 2 for x in range(10)]
print(squares)
# O snippet produz uma lista de dez elementos preenchida com quadrados de dez números inteiros começando em zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)


# Exemplo #2:
twos = [2 ** i for i in range(8)]
print(twos)
# O fragmento cria uma matriz de oito elementos que contém as oito primeiras potências de dois (1, 2, 4, 8, 16, 32, 64, 128)


# Exemplo #3:
odds = [x for x in squares if x % 2 != 0 ]
print(odds) 
# O fragmento faz uma lista com apenas os elementos ímpares da lista de squares.


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
 