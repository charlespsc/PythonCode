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

print("As instruções break e continue: mais exemplos")
print("A instrução break:\n")
largest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("O maior número é", largest_number)
else:
    print("Você não inseriu nenhum número.")

print("\nE agora a variação com continue: ")
largest_number = -99999999
counter = 0

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você nnão tem inseriu qualquer número.")
