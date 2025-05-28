#############################################################
### 4.5 Seção 5 - Criação de funções de vários parâmetros ###
#############################################################

# Bem-vindo à seção 5, onde analisaremos os seguintes exemplos de funções multiparâmetros: 
# - calculadora de IMC;
# - conversor de unidades;
# - testador de triângulos;
# - calculadora de áreas de triângulos;
# - fatorial;
# - Fibonacci e funções recursivas.

#################################################
### 4.5.1 Funções de Exemplo: avaliando o IMC ###
#################################################

# def imc(weight, height):
#     return weight / height ** 2
 
 
# print(imc(52.5, 1.65))
# # saídas: 19.218241582733813

# Avaliação do IMC e conversão de unidades imperiais em unidades métricas
# def bmi(weight, height):
#  # barra invertida (\) é usado para continuar a linha de código na próxima linha.
#  if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#     return None

#  return weight / height ** 2

# print(bmi(352.5, 1.65))
# # saídas: None


# Podemos escrever duas funções simples para converter unidades imperiais em unidades métricas. Vamos começar com libras.

# É um fato bem conhecido que 1 lb = 0.45359237 kg. Usaremos isso em nossa nova função.
# Essa é a nossa função auxiliar, chamada lb_to_kg:

# def lb_to_kg(lb):
#     return lb * 0.45359237

# print(lb_to_kg(1))
# saídas: 0.45359237


# E agora é hora de pés e polegadas: 1 pé = 0.3048 m, e 1 in = 2.54 cm = 0.0254 m.
# A função que escrevemos é chamada de ft_and_inch_to_m:
# def ft_and_inch_to_m(ft, inch):
#     return ft * 0.3048 + inch * 0.0254
 
# print(ft_and_inch_to_m(1, 1))
 
# # Vamos converter seis pés em metros:
# print(ft_and_inch_to_m(6, 0))

# É bem possível que às vezes você queira usar apenas pés sem polegadas. O Python vai ajudar? Claro que sim.
# Modificamos um pouco o código:
# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254
 
# print(ft_and_inch_to_m(6))
 
# Por fim, o código é capaz de responder à pergunta: qual é o IMC de uma pessoa de 5'7" de altura e pesando 176 libras?
# Este é o código que criamos:

# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254
 
# def lb_to_kg(lb):
#     return lb * 0.4535923
 
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None
 
#     return weight / height ** 2
 
# print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
 

############################################
### 4.5.2 Funções de exemplo: triângulos ###
############################################

# def is_a_triangle(a, b, c):
#  if a + b <= c:
#     return False
#  if b + c <= a:
#     return False
#  if c + a <= b:
#     return False
#  return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))
#Saídas:
# True
# False

# Podemos torná-lo mais compacto? Parece um pouco prolixo.
# Esta é uma versão mais compacta:
# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True
 
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))
# Saídas:
# True
# False


# Podemos compactá-lo ainda mais?
# Sim, podemos:
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))
# Saídas:
# True
# False

# Triângulos e o teorema de Pitágoras

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Digite o primeiro lado\'s comprimento: '))
# b = float(input('Entre no segundo lado\'s comprimento: '))
# c = float(input('Entre no terceiro lado\'s comprimento: '))

# if is_a_triangle(a, b, c):
#     print('Sim, pode ser um triângulo.')
# else:
#     print('Não, não pode ser um triângulo.')


# Na segunda etapa, tentaremos garantir que um determinado triângulo seja um triângulo de ângulo reto.

# Vamos precisar fazer uso do teorema de Pitágoras:

# c2 = a2 + b2

# Como podemos reconhecer qual dos três lados é a hipotenusa?

# A hipotenusa é o lado mais longo.

# Aqui está o código:
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2 
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#     if b > a and b > c:
#         return b ** 2 == a ** 2 + c ** 2
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))
# Saídas:
# True
# False


# Avaliando a área de um triângulo
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)
 
# print(area_of_triangle(1., 1., 2. ** .5))
 
############################################
### 4.5.3 Exemplos de funções: Fatoriais ###
############################################

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
# for n in range(1, 6):  # testando
#     print(n, factorial_function(n))
 
# Saídas:
# 1 1
# 2 2
# 3 6       
# 4 24
# 5 120


##################################
### 4.5.4 Números de Fibonacci ###
##################################

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
# for n in range(1, 10):  # testando
#     print(n, "->", fib(n))
 

######################
### 4.5.5 Recursão ###
######################

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum

# for n in range(1, 10):
#     print(n, "->", fib(n))

#############################
### 4.5.6 RESUMO DA SEÇÃO ###
#############################

# A função fatorial é um exemplo clássico de como o conceito de recursão pode ser colocado em prática:
# Implementação recursiva da função fatorial.
 
# def factorial(n):
#     if n == 1:    # O caso base (condição de rescisão).
#         return 1
#     else:
#         return n * factorial(n - 1)
 
 
# print(factorial(4)) # 4 * 3 * 2 * 1 = 24
 

############################
### 4.5.7 TESTE DA SEÇÃO ###
############################

# Pergunta 1: O que irá acontecer se você tentar rodar o trecho de código a seguir e porque?
# def factorial(n):
#     return n * factorial(n - 1)
 
# print(factorial(4))
# Resposta: O código resultará em um erro de RecursionError, 
# pois não há caso base definido para interromper a recursão, levando a uma chamada infinita da função.


# Pergunta 2: Qual é a saída do trecho de código?
# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3) 
 
# print(fun(25))
# Resposta: A saída será 56
 

