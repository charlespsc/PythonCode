#
# 3.3.2 Expressões lógicas

# var = 1
# # Exemplo 1:
# print(var > 0)
# print(not (var <= 0))
 
# # Exemplo 2:
# print(var != 0)
# print(not (var == 0))

# 3.3.3 Valores lógicos vs. bits únicos
 
# i = 1
# j = not i

# 3.3.4 Operadores bit a bit

# Aqui estão todos eles:

# & (e comercial) - conjunção bit a bit; E
# | (barra) - disjunção bit a bit; OU / OR
# ~ (til) - negação bit a bit; NOT
# ^ (circunflexo) ‒ bit a bit exclusivo ou (xor).

# 3.3.6 Deslocamento binário para a esquerda e deslocamento binário para a direita
# var = 17
# var_right = var >> 1
# var_left = var << 2
# print (var, var_left, var_right)

# 3.3.7 RESUMO DA SEÇÃO
# 
# 1. O Python é compatível com os seguintes operadores lógicos:
# 
# and → se ambos os operandos forem verdadeiros, a condição é verdadeira, por exemplo, (True and True) é True,
# or → se qualquer um dos operandos for verdadeiro, a condição é verdadeira, por exemplo, (True or False) é True,
# not → retorna falso se o resultado for verdadeiro e retorna verdadeiro se o resultado for falso, por exemplo, not True for False.
# 
# 
# 2. Você pode usar operadores bit a bit para manipular bits únicos de dados. Os seguintes dados de amostra:
# 
# x = 15, que é 0000 1111 em binário,
# y = 16, que é 0001 0000 em binário.
# 
# 
# será usado para ilustrar o significado dos operadores de bit a bit em Python. Analise os exemplos abaixo:
# 
# & faz um bit a bit e, por exemplo, x & y = 0 , que é 0000 0000 em binário,
# | faz um bit a bit ou, por exemplo, x | y = 31, que é 0001 1111 em binário,
# ˜ faz um bit a bit não, por exemplo, ˜ x = 240 *, que é 1111 0000 em binário,
# ^ faz um bit a bit xor, por exemplo, x ^ y = 31, que é 0001 1111 em binário,
# >> faz um deslocamento à direita bit a bit, por exemplo, y >> 1 = 8, que é 0000 1000 em binário,
# << faz um turno à esquerda bit a bit, por exemplo, y << 3 =, que é 1000 0000 em binário,
# * -16 (decimal do complemento de 2 assinado) - leia mais sobre a operação de complemento de Dois.



# 3.3.8 TESTE DA SEÇÃO

# Pergunta 1: Qual é a saída do trecho de código?

# x = 1
# y = 0
 
# z = ((x == y) and (x == y)) or not(x == y)
# print(not(z))
# 
# Output -> False

# Pergunta 2: Qual é a saída do trecho de código?


# x = 4
# y = 1
 
# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2
 
# print(a, b, c, d, e, f)
# Output -> 0 5 -5 1 1 16

