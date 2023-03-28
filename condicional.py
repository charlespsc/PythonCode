# Condições e execução condicional
#
print("Condições e execução condicional\n")
print("Execução condicional: o comando if")
#
# if sheep_counter >= 120:      # Avaliar uma expressão de teste
#     sleep_and_dream()         # Execute se a expressão de teste for verdadeira
#
# if sheep_counter >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()
#
print("Execução condicional: o comando if-else")
# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false
# 
# O comando if-else: mais execução condicional
# if the_weather_is_good:
#     go_for_a_walk()
# else:
#     go_to_a_theater()
# have_lunch()
#
# if the_weather_is_good:
#     go_for_a_walk()
#     have_fun()
# else:
#     go_to_a_theater()
#     enjoy_the_movie()
# have_lunch()
#
# Comandos if-else aninhados
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()
#
# O comando elif
# elif é usado para verificar mais de uma condição e parar quando
# a primeira declaração verdadeira é encontrada.
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()
# A maneira de montar instruções if-elif-else subsequentes é chamada de cascata.
#
print("Exemplo 1")
# Vamos começar com o caso mais simples: como identificar o maior de dois números:
#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)
#
#
# 
print("Exemplo 2")
# Agora, vamos mostrar um fato intrigante. 
# Python tem um recurso interessante - veja o código abaixo:
#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)
#
#
print("Exemplo 3")
# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)
#
#
print("Função interna do Python chamada max().")
# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)
 
# Imprimir o resultado.
print("O maior número é:", largest_number)
#
# Você também pode usar a função min()