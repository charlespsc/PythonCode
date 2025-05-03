print("For com range 10")
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um objeto iterável.
# A função range() gera uma sequência de números, que pode ser usada para iterar em um loop for.
# Por exemplo, range(10) gera números começando em 0, indo até (mas não incluindo) 10.
# Isso significa que o loop for irá iterar sobre os números 0, 1, 2, 3, 4, 5, 6, 7, 8 e 9.
# O loop for irá parar quando atingir o número 10, pois ele não está incluído na sequência.
# O loop for irá imprimir o valor de i em cada iteração.
for i in range(10):
   print("O valor de i é atualmente", i)

print("For com range 2 a 8")
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um objeto iterável.
# A função range() gera uma sequência de números, que pode ser usada para iterar em um loop for.
# Por exemplo, range(2, 8) gera números começando em 2, indo até (mas não incluindo) 8.
# Isso significa que o loop for irá iterar sobre os números 2, 3, 4, 5, 6 e 7.
# O loop for irá parar quando atingir o número 8, pois ele não está incluído na sequência.
# O loop for irá imprimir o valor de i em cada iteração.
for i in range(2, 8):
    print("O valor de i é atualmente", i)
 
print("For com range 2 a 8 com passo 2")
# O terceiro argumento na função range() é o passo, que determina o incremento entre os números gerados.
# Por exemplo, range(2, 8, 2) gera números começando em 2, indo até (mas não incluindo) 8, com um incremento de 2.
# Isso significa que o loop for irá iterar sobre os números 2, 4 e 6.
# O loop for irá parar quando atingir o número 8, pois ele não está incluído na sequência.
# O loop for irá imprimir o valor de i em cada iteração.
for i in range(2, 8, 2):
    print("O valor de i é atualmente", i)


# A variável expo é usada como uma variável de controle para o loop e indica o valor atual do expoente
# A exponenciação em si é substituída pela multiplicação por dois. 
# Como 2^0 é igual a 1 --- 2 × 1 é igual a 2^1 --- 2 × 2^1 é igual a 2^2 e assim por diante.
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2
