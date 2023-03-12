
#uma únicaif declaração, por exemplo:
x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.
    

#uma série de if declarações, por exemplo:
#Cada ifdeclaração é testada separadamente.

x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
    

#uma if-elsedeclaração, por exemplo:

x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.
    

#uma série de if declarações seguidas por um else, por exemplo:
#Cada if é testado separadamente. O corpo de else é executado se o último if for False.
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")
    

# A if-elif-elsedeclaração, por exemplo:
#Se a condição if for False, o programa verifica as condições dos elif blocos subsequentes -
# o primeiro elif bloco que True é executado. 
# Se todas as condições forem False, o else bloco será executado.
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

#Declarações condicionais nested, por exemplo:

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")

