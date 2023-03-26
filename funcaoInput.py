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
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
