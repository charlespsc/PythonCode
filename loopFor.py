# Se você quiser usar o loop while, pode ser assim:

# i = 0
# while i < 100:
#     # do_something()
#     i += 1
    
# for i in range(100):
#     # do_something()
# #     pass
# print("\n### Função RANGE ###")
# for i in range(10):
#    print("O valor de i é atualmente", i)

# print("\n### Função range com um argumento ###")
# for i in range(2, 8):
#     print("O valor de i é atualmente", i)
    
# # Função range com 3 argumento (o terceiro argumento é um incremento).
# # for i in range(2, 9, 3):
# #   print("O valor de i é atualmente", i)

# #     # Assim como aqui - não haverá saída:

#     # Nota: se o conjunto gerado pela função range() estiver vazio, o loop não executará seu corpo.
# for i in range(1, 1):
#     print("O valor de i é atualmente", i)
    
# for i in range(2, 1):
#     print("O valor de i é atualmente", i)
    
# print("\n### Variável expo é usada como uma variável de controle para o loop e indica o valor atual do expoente. ###")
# power = 1
# for expo in range(16):
#   print("2 à potência de", expo, "é", power)
#   power *= 2

# # 3.2.8 As instruções break e continue

# # break - exemplo

# print("\n ### The break instrução: ###")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro do laço.", i)
# print("Fora do loop.")


# # continue - exemplo

# print("\n### The continue instrução: ###")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro do laço.", i)
# print("Fora do loop.")

# print("As instruções break e continue: mais exemplos")
# print("A instrução break:\n")
# largest_number = -99999999
# counter = 0

# while True:
#     number = int(input("Digite um número ou digite -1 para terminar o programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("O maior número é", largest_number)
# else:
#     print("Você não inseriu nenhum número.")

# print("\nE agora a variação com continue: ")
# largest_number = -99999999
# counter = 0

# number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

# if counter:
#     print("O maior número é",  largest_number)
# else:
#     print("Você nnão tem inseriu qualquer número.")
#
#
# ------ 3.2.16 RESUMO DA SEÇÃO ------ #

# Exemplo 1
# while True:
#     print("Preso em um loop infinito.")
 
# # Exemplo 2
# counter = 5
# while counter > 2:
#     print(counter)
#     counter -= 1
#
# Exemplo 1
# word = "Python"
# for letter in word:
#     print(letter, end="*")
 
# # Exemplo 2
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#
#
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "I":
#         break
#     print(letter, end="")
    
# text = "pyxpyxpyx"
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")

# n = 0
 
# while n != 3:
#     print(n)
#     n += 1
# else:
#     print(n, "else")
 
# print()
 
# for i in range(0, 3):
#     print(i)
# else:
#     print(i, "else")
    
#  sintaxe de range() tem a seguinte aparência: range(start, stop, step), em que:

# for i in range(3):
#     print(i, end=" ")  # Outputs: 0 1 2
 
# for i in range(6, 1, -2):
#     print(i, end=" ")  # Outputs: 6, 4, 2
 
#  3.2.17 TESTE DA SEÇÃO

#  Pergunta 1: Crie um loop for com contagem de 0 a 10 e imprima números ímpares na tela. Use o esqueleto abaixo:
# for i in range(1, 11):
#     # Linha de código.
#         # Linha de código.
# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)

# Pergunta 2: Crie um loop while que conta de 0 a 10 e imprime números ímpares na tela. Use o esqueleto abaixo:
# x = 1
# while x < 11:
#     # Linha de código.
#         # Linha de código.
#     # Linha de código.
# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# Pergunta 3: Crie um programa com um loop for e uma declaração de break. 
# O programa deve iterar os caracteres em um endereço de e-mail, sair do loop quando atingir o símbolo @ e imprimir a peça antes de @ em uma linha. 
# Use o esqueleto abaixo:

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Linha de código.
#     # Linha de código.

# for ch in "john.smith@pythoninstitute.org":
#      if ch == "@":
#          break
#      print(ch, end="")
#
#     
# Pergunta 4: Crie um programa com um loop for e uma declaração continue. 
# O programa deve repetir uma sequência de dígitos, substituir cada 0 por x e imprimir a sequência modificada na tela. 
# Use o esqueleto abaixo:

# for digit in "0165031806510":
#     if digit == "0":
#         # Linha de código.
#         # Linha de código.
#     # Linha de código.
#
#
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# Pergunta 5: Qual é a saída do código a seguir?
# n = 3
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)
#
#
# n = 3
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)
#
#
# Pergunta 6: Qual é a saída do código a seguir?

# n = range(4)
 
# for num in n:
#     print(num - 1)
# else:
#     print(num)
    
    
#Pergunta 7: Qual é a saída do código a seguir?

# for i in range(0, 6, 3):
#     print(i)