# O Python interpreta a verdade de uma condição e observe que essas duas formas são equivalentes:
#
# while number != 0: 
# while number:
#

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)


# O que acontece se você não usar o operador de comparação?
# counter = 5
# while counter:
#     print("Dentro do laço.", counter)
#     counter -= 1
# print("Fora do circuito.", counter)
