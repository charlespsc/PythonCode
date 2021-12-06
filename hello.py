print ("A função print()")
print ("Hello, Python!")

# A função print() - instruções
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

# A função print() - instruções (função vazia)
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# A função print() - os carateres de escape e de newline
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
print("\\")

#A função print() - utilizar múltiplos argumentos
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#A função print() - a forma posicional de passar os argumentos
print("My name is", "Python.")
print("Monty Python.")

# A função print() - os argumentos de keyword (end)
print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is", "Python.", end="\n")
print("Monty Python.")

#A função print() - os argumentos de keyword (sep)
print("My", "name", "is", "Monty", "Python.", sep="->")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print("    *\n" "   * *\n" "  *   *\n" " *     *\n""***   ***\n""  *   *\n""  *   *\n""  *****")

print ("string" * 2)


# 2.2.1.2 Literais - os dados em si
print("2")
print(2)

# Inteiros: números octais e hexadecimais
print(0o123)
print(0x123)

# Inteiros vs floats
# 4 é um número inteiro 
# 4.0 é um floating-point
# 
# Floating pode usar NOTAÇÃO CIENTÍFICA
# Exe.: 3e8
print ( )
# Strings (aspas dentro da string)
print("I like \"Monty Python\"")
print('I like "Monty Python"')
print ( )
print('I\'m Monty Python.')
print("I'm Monty Python.")

# Valores Booleanos
print(True > False)
print(True < False)

print ("I\'m")
print ('""learning""')
print ('"""Python"""')

#Python como uma calculadora
print(2+2)

#Operadores aritméticos: exponenciação
#Um sinal ** (duplo asterisco) é um operador de exponenciação (potência)
# exemplo, 2 ** 3

print ("Operadores aritméticos: divisão inteira")
#Um sinal // (dupla barra) é um operador de divisão inteira.
print(6 // 4)
print(6. // 4)


print ("### VARIÁVEIS ###")
var = "1 mil reais"
print(var)

var = "3.8.5"
print("Python version: " + var)

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

print ("Resolução de problemas matemáticos simples")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

print ()
print ("LAB: Variáveis")

jonh = 3 
mary = 5
adam = 6
total_apples = jonh + mary + adam

print (jonh, mary, adam, sep=",")
print (total_apples)

print ()
print ("Operadores de atalho")

print("LAB 2.4.1.9 - Variáveis: um conversor simples")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.61*miles
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

var = 2
print(var)

var = 3
print(var)

var += 1
print(var)

var = "007"
print("Agent " + var)

var = 2
var = 3
print(var)

a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)

#This is a test program.
x = 1
y = 2
# y = y + x
print(x + y)

#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

print ("Goodbye")
#this is the end of the program that computes the number of seconds in 3 hour

# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")

# print("String #1")
print("String #2")

# This is
#a multiline
#comment.
print("Hello!")

print("")
print("A funcao input()")


print("Tell me anything...")
#anything = input()
#print("Hmm...", anything, "... Really?")

#fnam = input("May I have your first name, please? ")
#lnam = input("May I have your last name, please? ")
#print("Thank you.")
#print("\nYour name is " + fnam + " " + lnam + ".")

#Replicação
print ("James" * 3)
print (3 * "Ana" * 3)
print (5 * "2")
print ("2" * 5)
print (5 * "2")
print (5 * 2)

#Este programa simples "desenha" um retângulo, fazendo uso de um antigo operador (+) num novo papel:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Conversão de tipo: str()
#
#
### LAB - input e Output SIMPLES ###
#
# input a float value for variable a here
#leg_a = float(input("Input first leg length: "))
# input a float value for variable b here
#leg_b = float(input("Input second leg length: "))
#
# output the result of addition here
#print("SOMA: " + str(leg_a + leg_b))
# output the result of subtraction here
#print("SUBTRAIR: " + str(leg_a - leg_b))
# output the result of multiplication here
#print("MULTIPLICAR: " + str(leg_a * leg_b))
# output the result of division here
#print("DIVIDIR: " + str(leg_a / leg_b))
#
#print("\nThat's all, folks!")
#
#
#
#name = input("Enter your name: ")
#print("Hello, " + name + ". Nice to meet you!")
#
#print("\nPress Enter to end the program.")
#input()
#print("THE END.")

#num_1 = input("Enter the first number: ") # Enter 12
#num_2 = input("Enter the second number: ") # Enter 21
#
#print(num_1 + num_2) # the program returns 1221


#Exercício 1
#Qual é o output do seguinte snippet?
#x = int(input("Enter a number: ")) # The user enters 2
#print(x * "5")

print (123 + 0.0)
print (1 ** 2 ** 3)

print ( 1 // 2 * 3 )

print ("questao")
x = int(input(2))
y = int(input(4))

print (x + y)