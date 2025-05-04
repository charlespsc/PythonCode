
# Esse é um exemplo de uso do for-else
# O loop for pode ter um bloco else
# O bloco else é executado quando o loop termina normalmente, ou seja, não foi interrompido por um break.
# O bloco else não é executado se o loop for interrompido por um break.
# Exemplo de uso do for-else
for i in range(5):
 print(i)
else:
 print("else:", i)


# A condição do for é False no início
# O corpo do loop não será executado aqui. 
# Quando o corpo do loop não é executado, a variável de controle retém o valor que tinha antes do loop.
# i = 111

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
