# print("Condições e execução condicional\n")
# print("Execução condicional: o comando if")
# #
# # if sheep_counter >= 120:      # Avaliar uma expressão de teste
# #     sleep_and_dream()         # Execute se a expressão de teste for verdadeira
# #
# # if sheep_counter >= 120:
# #     make_a_bed()
# #     take_a_shower()
# #     sleep_and_dream()
# # feed_the_sheepdogs()
# #
# print("Execução condicional: o comando if-else")
# # if true_or_false_condition:
# #     perform_if_condition_true
# # else:
# #     perform_if_condition_false
# # 
# print ("O comando if-else: mais execução condicional")
# # if the_weather_is_good:
# #     go_for_a_walk()
# # else:
# #     go_to_a_theater()
# # have_lunch()
# #
# # if the_weather_is_good:
# #     go_for_a_walk()
# #     have_fun()
# # else:
# #     go_to_a_theater()
# #     enjoy_the_movie()
# # have_lunch()
# #
# print ("Comandos if-else aninhados")
# # if the_weather_is_good:
# #     if nice_restaurant_is_found:
# #         have_lunch()
# #     else:
# #         eat_a_sandwich()
# # else:
# #     if tickets_are_available:
# #         go_to_the_theater()
# #     else:
# #         go_shopping()
# # #
# print ("O comando elif")
# # elif é usado para verificar mais de uma condição e parar quando
# # a primeira declaração verdadeira é encontrada.
# #
# # if the_weather_is_good:
# #     go_for_a_walk()
# # elif tickets_are_available:
# #     go_to_the_theater()
# # elif table_is_available:
# #     go_for_lunch()
# # else:
# #     play_chess_at_home()
# #
# # A maneira de montar instruções if-elif-else subsequentes é chamada de cascata.
# #
# print("Exemplo 1")
# # Vamos começar com o caso mais simples: como identificar o maior de dois números:
# #Ler dois números
# number1 = int(input("Digite o primeiro número: "))
# number2 = int(input("Digite o segundo número: "))
 
# # Escolha o número maior
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
 
# # Imprimir o resultado
# print("O maior número é:", larger_number)
# #
# #
# # 
# print("Exemplo 2")
# # Agora, vamos mostrar um fato intrigante. 
# # Python tem um recurso interessante - veja o código abaixo:
# #Ler dois números
# number1 = int(input("Digite o primeiro número: "))
# number2 = int(input("Digite o segundo número: "))
 
# # Escolha o número maior
# if number1 > number2: larger_number = number1
# else: larger_number = number2
 
# # Imprimir o resultado
# print("O maior número é:", larger_number)
# #
# #
# print("Exemplo 3")
# # Leia três números
# number1 = int(input("Digite o primeiro número: "))
# number2 = int(input("Digite o segundo número: "))
# number3 = int(input("Digite o terceiro número: "))
 
# # Assumimos temporariamente que o primeiro número é o maior deles.
# # Em breve verificaremos isso.
# largest_number = number1
 
# # Nós verificamos se o segundo número é maior que o maior_número atual
# # e atualize o maior_número, se necessário.
# if number2 > largest_number:
#     largest_number = number2
 
# # Nós verificamos se o terceiro número é maior que o maior_número atual
# # e atualize o maior_número, se necessário.
# if number3 > largest_number:
#     largest_number = number3
 
# # Imprimir o resultado
# print("O maior número é:", largest_number)
# #
# #
# print("Função interna do Python chamada max().")
# # Leia três números.
# number1 = int(input("Digite o primeiro número: "))
# number2 = int(input("Digite o segundo número: "))
# number3 = int(input("Digite o terceiro número: "))
 
# # Verifique qual dos números é o maior
# # e passe-o para a variável de número_maior.
 
# largest_number = max(number1, number2, number3)
 
# # Imprimir o resultado.
# print("O maior número é:", largest_number)
# #
# # Você também pode usar a função min()

# ###  RESUMO DA SEÇÃO   ###
# # Quando você deseja executar algum código apenas se uma determinada condição for atendida, 
# # você pode usar uma declaração condicional:

# # uma única declaração if, por exemplo:
# x = 10
 
# if x == 10: # condição
#     print("x é igual a 10")  # Executado se a condição for True.

# # uma série de declarações if, por exemplo:
# x = 10
 
# if x > 5: # condição um
#     print("x é maior que 5")  # Executado se a condição um for True.
 
# if x < 10: # condição dois
#     print("x é menor que 10")  # Executado se a condição dois for True.
 
# if x == 10: # condição três
#     print("x é igual a 10")  # Executado se a condição três for True.
    
# # Cada declaração if é testada separadamente.

# # uma declaração if-else, por exemplo:
# x = 10
 
# if x < 10: # condição
#     print("x é menor que 10")  # Executado se a condição for True.
 
# else:
#     print("x é maior ou igual a 10")  # Executado se a condição for False.

# # uma série de instruções if seguidas de um else, por exemplo:
# x = 10
 
# if x > 5: # condição um
#     print("x é maior que 5")  # Executado se a condição um for True.
 
# if x < 10: # condição dois
#     print("x é menor que 10")  # Executado se a condição dois for True.
 
# if x == 10: # condição três
#      print("x é igual a 10")  # Executado se a condição três for True.
     
# # Cada um if é testado separadamente. O corpo do else é executado se o último if for False.

# # A declaração if-elif-else, por exemplo:
# x = 10
 
# if x == 10: # True
#     print("x == 10")
 
# if x > 15: # False
#     print("x > 15")
 
# elif x > 10: # False
#     print("x > 10")
 
# elif x > 5: # True
#     print("x > 5")
 
# else:
#     print("senão não será executado")

# # Se a condição para if for False, o programa verifica as condições dos blocos elif subsequentes
# # - o primeiro bloco elif que é True é executado. 
# # Se todas as condições forem False, o bloco else será executado.

# # Instruções condicional aninhadas, por exemplo:
# x = 10
 
# if x > 5: # True
#     if x == 6: # False
#         print("aninhado: x == 6")
#     elif x == 10: # True
#         print("aninhado: x == 10")
#     else:
#         print("aninhado: else")
# else:
#     print("else")

# TESTE DA SEÇÃO
# Pergunta 1: Qual é a saída do trecho de código?
x = 5
y = 10
z = 8
 
print(x > y)
print(y > z)

# Pergunta 2: Qual é a saída do trecho de código?

x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)

# Pergunta 3: Qual é a saída do trecho de código?

x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)

# Pergunta 4: Qual é a saída do trecho de código?

x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

# Pergunta 5: Qual é a saída do trecho de código?

x = "1"
 
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
 
# Pergunta 6: Qual é a saída do trecho de código?

x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")