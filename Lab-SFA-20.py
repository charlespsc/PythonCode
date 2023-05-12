# 3.6.6   LAB   Operações com listas ‒ básico

# Cenário
# 
# Imagine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. 
# Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.

# Sua tarefa é escrever um programa que remova todas as repetições de números da lista.
# O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.

# Nota: suponha que a lista de origem seja codificada dentro do código - você não precisa inseri-la no teclado.
# Claro, você pode melhorar o código e adicionar uma parte que possa conversar com o usuário e obter todos os dados dele.

# Dica: recomendamos que você crie uma nova lista como uma área de trabalho temporária. Você não precisa atualizar a lista in situ.

# Não fornecemos dados de teste, pois isso seria muito fácil. Você pode usar o nosso esqueleto.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Sua tarefa é escrever um programa que remova todas as repetições de números da lista.
new_list = [] 

for numero in my_list:
    if numero not in new_list:
        new_list.append(numero)

print("Nova Lista: ", new_list)

# Claro, você pode melhorar o código e adicionar uma parte que possa conversar com o usuário e obter todos os dados dele. 
user_list = []  # Criando uma lista vazia.

user_list.append(int(input("\nDigite o primeiro números: ")))
user_list.append(int(input("Digite o segundo números: ")))
user_list.append(int(input("Digite o terceiro números: ")))
user_list.append(int(input("Digite o quarto números: ")))
user_list.append(int(input("Digite o quinto números: ")))

user_new_list = [] 

for userNum in user_list:
    if userNum not in user_new_list:
        user_new_list.append(userNum)

print("\nLista do usuário: ", user_new_list)

######################################################################
print("\nA lista com os elementos exclusivos aqui")
print(my_list)


