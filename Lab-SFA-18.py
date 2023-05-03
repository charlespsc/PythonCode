# 3.4.6   LAB   Básico de listas

# Cenário:
    
# Era uma vez um chapéu. O chapéu não continha coelhos, mas uma lista de cinco números: 1, 2, 3, 4 e 5.

numbers = [1, 2, 3, 4, 5]
print("\nA lista original é ", numbers) 

newNumber = int(input("\nInsira um número inteiro: "))
numbers[2] = newNumber

print("\nA lista com novo número é ", numbers) 

print("Deletando o último número...\n")
del numbers[-1]

print ("Comprimento da nova lista:", len (numbers)) 

