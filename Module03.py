print ("Comparacao: operador de igualdade")
print ("Qual o resultado?")
print ("1 == 2 is ->", 1 == 2)
var = 0  # Assigning 0 to var
print(var == 0)
var = 1  # Assigning 1 to var
print(var == 0)
print ()
print ("Desigualdade: o operador nao igual a (!=)")
var = 0  # Assigning 0 to var
print(var != 0)
var = 1  # Assigning 1 to var
print(var != 0)

print ("Operadores de comparação: maior que ou igual a >=")

#LAB 3.1.4
#N = int(input("Number N: ")) # False se N for menor que 100, e True Se n for >= 100
#print(N >= 100)

# CONDICIONAL - if
#if sheep_counter >= 120:
#    make_a_bed()
#    take_a_shower()
#    sleep_and_dream()
#feed_the_sheepdogs()

# CONDICIONAL - else 
#if true_or_false_condition:
#    perform_if_condition_true
#else:
#    perform_if_condition_false

#DECISAO EM PYTHON

#exemplo 1
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

#exemplo 2
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

#exemplo 3

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

