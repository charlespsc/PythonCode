### TESTE DO MÓDULO 3 ###

# Pergunta 1
# Um operador capaz de verificar se dois valores são iguais é codificado como:
# ==

# Pergunta 2
# O valor eventualmente atribuído a x é igual a:
# x = 1
# x = x == x
# print(x)
# output: True

# Pergunta 3
# Quantas estrelas (*) serão mandadas ao console pelo seguinte trecho de código?
# i = 0
# while i <= 3 :
#     i += 2
#     print("*")
# output: 2

# Pergunta 4
# Quantas estrelas (*) serão mandadas ao console pelo seguinte trecho de código?
# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")
# output: 1

# Pergunta 5
# Quantos hashes (#) o snippet a seguir enviará para o console?
# for i in range(1):
#     print("#")
# else:
#     print("#")
# output: 2

# Pergunta 6
# Quantos hashes (#) o snippet a seguir enviará para o console?
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")
# output: 3

# Pergunta 7
# Quantos hashes (#) o snippet a seguir enviará para o console?
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
# output: 4

# Pergunta 8
# Que valor será atribuído à variável x?
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)
# output: True

# Pergunta 9
# Qual é a saída do seguinte snippet?
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b

# print(c + d + e)
# output: 2

# Pergunta 10
# Qual é a saída do seguinte snippet?
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])
# output: 1

# Pergunta 11
# Qual é a saída do seguinte snippet?
# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])
# output: [2]

# Pergunta 12
# A segunda tarefa:
# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)
# output: [2, 1, 0]
# reverte a lista

# Pergunta 13
# Após a execução do seguinte código, a soma de todos os elementos de vals será igual a:
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)
# output: [1, 1, 2]
# a soma é 1 + 1 + 2 = 4

# Pergunta 14
# Dê uma olhada no snippet e escolha as afirmações verdadeiras: (selecione duas respostas)
# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(nums)
# print(vals)
# output: [1, 3]
# nums é replicado e atribuído a vals, então quando vals é alterado, nums também é alterado.
# nums e vals são referências para o mesmo objeto.

# Pergunta 15
# Quais das seguintes frases são verdadeiras? (Selecione duas respostas)
# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(nums) # output: [1, 2, 3]
# print(vals) # output: [ ]
# nums e vals são referências para objetos diferentes.
# nums é maior que vals.

# Pergunta 16
# Qual é a saída do seguinte snippet?
# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)
# output: [3, 2, 1]

# Pergunta 17
# Qual é a saída do seguinte snippet?
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
# output: [1, 1, 1, 1, 2, 3]

# Pergunta 18
# Quantos elementos a lista my_list contém?
# my_list = [i for i in range(-1, 2)]
# print(my_list)
# output: 3

# Pergunta 19
# Qual é a saída do seguinte snippet?
# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
# output: 6

# Pergunta 20
# Qual é a saída do seguinte snippet?
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])
# output: IndexError: list index out of range
