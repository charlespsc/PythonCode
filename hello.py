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
