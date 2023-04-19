print("Fazendo um loop no seu código com while")
#
# Você concorda com a afirmação apresentada abaixo?
#
# enquanto há algo para fazer
#     faça isso
#
# while conditional_expression:
#     instruction_one
#     instruction_two
#     instruction_three
#     ...
#     ...
#     instruction_n

print("Um loop infinito")
#while True:
#    print("Estou preso dentro de um loop.")
#
#
# Armazene o maior número atual aqui.
# largest_number = -999999999
 
# # Insira o primeiro valor.
# number = int(input("Digite um número ou digite -1 para parar: "))
 
# # Se o número não for igual a -1, continue.
# while number != -1:
#     # O número é maior que o maior_número?
#     if number > largest_number:
#         # Sim, atualize o maior_número.
#         largest_number = number
#     # Insira o próximo número.
#     number = int(input("Digite um número ou digite -1 para parar: "))
 
# # Imprima o maior número.
# print("O maior número é:", largest_number)
#
# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
# odd_numbers = 0
# even_numbers = 0
 
# # Leia o primeiro número.
# number = int(input("Digite um número ou digite 0 para parar: "))
 
# # 0 termina a execução.
# while number != 0:
#     # Verifique se o número é ímpar.
#     if number % 2 == 1:
#         # Aumente o contador odd_numbers.
#         odd_numbers += 1
#     else:
#         # Aumente o contador even_numbers.
#         even_numbers += 1
#     # Leia o número seguinte.
#     number = int(input("Digite um número ou digite 0 para parar: "))
 
# # Imprimir resultados.
# print("Números ímpares contam:", odd_numbers)
# print("Números pares contam:", even_numbers)
 
# counter = 5
# while counter != 0:
#     print("Dentro do laço.", counter)
#     counter -= 1
# print("Fora do circuito.", counter)

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)