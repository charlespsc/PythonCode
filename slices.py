#3.6.2 Os poderes do fatiamento3.6.2 Os poderes do fatiamento
# 
# # Python que permite fazer uma cópia totalmente nova de uma lista ou de partes de uma lista.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
# Saída: [1]

# Explicação de fatiamento:
# my_list[start:end]
# start ao end -1
### start é o índice do primeiro elemento incluído na fatia;
### end é o índice do primeiro elemento não incluído na fatia.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
# Saída: [8, 6]


# 3.6.3 Fatias - índices negativos

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
# Saída: [8, 6, 4]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
# Saída: []

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
# Saída: [10, 8, 6]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
# Saída: [4, 2]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
# Saída: [10, 8, 6, 4, 2]

## Mais sobre a instrução del
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
# Saída: [10, 4, 2]

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
# Saída: []

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
# Saída: NameError: name 'my_list' is not defined


## 3.6.4 Os operadores in e not in

# elem in my_list
# elem not in my_list
 
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
# Saída: False, True, True

# 3.6.5 Listas - alguns programas simples
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
# Saída: 17

# O código pode ser reescrito para utilizar o formulário recém-introduzido do loop for:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)
# Saída: 17

# Se precisar economizar energia do computador, use uma fatia:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)
# Saída: 17

# Agora vamos encontrar a localização de um determinado elemento dentro de uma lista:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
# Saída: Elemento encontrado no índice 4


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)
# Saída: 3