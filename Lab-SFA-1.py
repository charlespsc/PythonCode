# LAB   Variáveis
# Cenário
# Aqui está uma breve história:
#
# Era uma vez em Appleland, John tinha três maçãs, Maria cinco maçãs e Adam tinha seis maças. Todos ficaram muito felizes e viveram por muito tempo. Fim da história.
#
# Sua tarefa:
#
# 1 - crie as variáveis: john, mary e adam;
# 2 - atribuir valores às variáveis. Os valores devem ser iguais aos números de fruto possuído por John, Mary e Adam, respectivamente;
# 3 - tendo armazenado os números nas variáveis, imprimindo as variáveis em uma linha e separando cada uma delas com uma vírgula;
# 4 - Agora, crie uma nova variável chamada total_apples igual à adição das três variáveis anteriores.
# 5 - imprima o valor armazenado em total_apples no console;
# 6 - experimente com seu código: crie novas variáveis, atribua valores diferentes a elas e execute várias operações aritméticas nelas (por exemplo, +, -, *, /, //, etc.). Tente imprimir uma sequência de caracteres e um número inteiro juntos em uma linha, por exemplo, "Número total de maças:" e total_apples.
#
#
# john = 3
# mary = 5
# adam = 6
# total_apples = john + mary + adam

# print(john, ",",mary,",", adam)
# print("Total Apples: ", total_apples)
#
#
print("Resposta do exemplo: \n")
#
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)

peter = 12.5
suzy = 2
print(peter / suzy)
print("Número total de maçãs:", total_apples)
