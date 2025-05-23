my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
 
for i in range(len(my_list) - 1):  # precisamos de (5 - 1) comparações
    if my_list[i] > my_list[i + 1]:  # comparar elementos adjacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Se acabarmos aqui, nós temos que trocar os elementos.
 
print(my_list)  
# Saída: [8, 6, 2, 4, 10]


my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
 

# 3.5.3 A ordenação por bolhas - versão interativa
my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
 val = float(input("Entre com a lista de elementos:"))
 my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# Saída: [2, 4, 6, 8, 10]


# Python tem seus próprios mecanismos de classificação. 
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
 
# Saída: [2, 4, 6, 8, 10]



## 3.5.4 RESUMO DA SEÇÃO

# 1. Você pode usar o método sort() para classificar elementos de uma lista, por exemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
 
# 2. Há também um método de lista chamado revers(), que você pode usar para reverter a lista, por exemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

# 3. Você pode usar o método sort() para classificar uma lista de strings, por exemplo:
lst = ["banana", "maçã", "laranja", "uva"]
print(lst)
lst.sort()
print(lst)  # outputs: ['banana', 'laranja', 'maçã', 'uva']

# 4. Você pode usar o método sort() para classificar uma lista de tuplas, por exemplo:
lst = [(1, 2), (3, 1), (2, 3)]
print(lst)
lst.sort()
print(lst)  # outputs: [(1, 2), (2, 3), (3, 1)]

# 5. Você pode usar o método sort() para classificar uma lista de dicionários, por exemplo:
lst = [{"nome": "João", "idade": 25}, {"nome": "Maria", "idade": 30}, {"nome": "José", "idade": 20}]
print(lst)
lst.sort(key=lambda x: x["idade"])
print(lst)  # outputs: [{'nome': 'José', 'idade': 20}, {'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}]

# 6. Você pode usar o método sort() para classificar uma lista de números, por exemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.sort(reverse=True)
print(lst)  # outputs: [5, 4, 3, 2, 1]


### 3.5.5 TESTE DA SEÇÃO ###

# Pergunta 1: Qual é a saída do trecho de código?
lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)
 
# Pergunta 2: Qual é a saída do trecho de código?
a = 3
b = 1
c = 2
 
lst = [a, c, b]
lst.sort()
 
print(lst)
 
# Pergunta 3: Qual é a saída do trecho de código?
a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst)
 
