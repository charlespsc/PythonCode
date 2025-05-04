# O loop while pode ter um bloco else
# O bloco else é executado quando o loop termina normalmente, ou seja, não foi interrompido por um break.
# O bloco else não é executado se o loop for interrompido por um break.
# Exemplo de uso do while-else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


# A condição do while é False no início
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)