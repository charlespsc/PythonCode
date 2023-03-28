# Funçao input()
#
# print("Conta-me qualquer coisa...")
# anything = input()
# print("Hum...", anything, "... Realmente?\n")
# #
# #
# # A função input() com um argumento
# #
# anything = input("Conta-me qualquer coisa...\n")
# print("Hum...", anything, "...Realmente?")
#
#
# O resultado da função input()
#
# anything = input("Digite um número: ")
# something = anything ** 2.0
# print(anything, "elevado a 2 é", something)
#
#  Digite um número: 2
# Traceback (most recent call last):
#   File "/Users/charlespereira/Documents/Repository Github/PythonCode/funcaoInput.py", line 17, in <module>
#     something = anything ** 2.0
#                 ~~~~~~~~~^^~~~~
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# -----------------------------------------------------------------------------------------------------------
#
# Conversão de tipo (tipo de conversões)
#
# anything = float(input("Digite um número: "))
# something = anything ** 2.0
# print(anything, "elevado a 2 é", something)
# #
# leg_a = float(input("Insira o comprimento da primeira perna: "))
# leg_b = float(input("Insira o comprimento da segunda perna: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("O comprimento da hipotenusa é", hypo)
# #
# leg_a = float(input("Insira o comprimento da primeira perna: "))
# leg_b = float(input("Insira o comprimento da segunda perna: "))
# print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)
#
#
# Operadores de string
#
# fnam = input("Posso ter seu primeiro nome, por favor? ")
# lnam = input("Posso ter seu sobrenome, por favor? ")
# print("Obrigado!")
# print("\nSeu nome é " + fnam + " " + lnam + ".")
#
# Replicação
#
# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")
#
#
# Conversões de tipo mais uma vez concluídas
#
# O triângulo de ângulo direito novamente
# leg_a = float(input("Insira o comprimento da primeira perna: "))
# leg_b = float(input("Insira o comprimento da segunda perna: "))
# print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))
#
# name = input("Digite seu nome: ")
# print("Olá, " + name + ". Prazer em conhecê-lo!")
 
# print("\nPressione Enter para finalizar o programa.")
# input()
# print("O FIM.")
#
# num_1 = input("Digite o primeiro número: ") # Digite 12
# num_2 = input("Digite o segundo número: ") # Digite 21
 
# print(num_1 + num_2) # o programa retorna 1221
#
# my_input = input("Enter something: ") # Exemplo de entrada: Olá
# print(my_input * 3) # Saída esperada: OláOláOlá
 
# x = int(input("Digite um número: ")) # O usuário digita 2
# print(x * "5")
 
# x = input("Digite um número: ") # O usuário digita 2
# print(type(x))
# print (1 /1)

# x = 1
# y = 2
# z = x
# x = y
# y = z
# print(x, y)

# x = input()
# y = input()
# print(x + y)
 
 
# x = int(input())
# y = int(input())
 
# x = x // y
# y = y // x
 
# print(y)

# x = int(input())
# y = int(input())
 
# x = x / y
# y = y / x
 
# print(y)

# x = int(input())
# y = int(input())
 
# x = x % y
# x = x % y
# y = y % x
 
# print(y)

# x = input()
# y = int(input())
 
# print(x * y)

# z = y = x = 1
# print(x, y, z, sep='*')

# y = 2 + 3 * 5.
# print(Y)

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

x = int(input())
y = int(input())
 
print(x + y)
