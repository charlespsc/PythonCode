# Se você quiser usar o loop while, pode ser assim:

# i = 0
# while i < 100:
#     # do_something()
#     i += 1
    
# for i in range(100):
#     # do_something()
#     pass

# for i in range(10):
#    print("O valor de i é atualmente", i)

# # Função range com um argumento.
# for i in range(2, 8):
#     print("O valor de i é atualmente", i)
    
# Função range com 3 argumento (o terceiro argumento é um incremento).
# for i in range(2, 9, 3):
#   print("O valor de i é atualmente", i)

#     # Assim como aqui - não haverá saída:

    # Nota: se o conjunto gerado pela função range() estiver vazio, o loop não executará seu corpo.
    # for i in range(1, 1):
    #     print("O valor de i é atualmente", i)
    #
    # for i in range(2, 1):
    #     print("O valor de i é atualmente", i)
    #
# A variável expo é usada como uma variável de controle para o loop e indica o valor atual do expoente.
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2