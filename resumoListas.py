# 3.6.7 RESUMO DA SEÇÃO

# 1. Se você tiver uma lista list_1, a seguinte atribuição: list_2 = list_1 não faz uma cópia da lista list_1,
# mas faz com que as variáveis list_1 e list_2 apontem para uma mesma lista na memória. Por exemplo:
vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one) # outputs: ['carro', 'bicicleta', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # exclui 'carro'
print(vehicles_two) # outputs: ['bicicleta', 'motor']
 

# 2. Se quiser copiar uma lista ou parte da lista, você pode fazer isso dividindo:
colors = ['vermelho', 'verde', 'laranja']
 
copy_whole_colors = colors[:]  # copie a lista inteira
copy_part_colors = colors[0:2]  # copiar parte da lista
 

# 3. Você também pode usar índices negativos para executar fatias. Por exemplo:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
 
# 4. Os start de end e fim são opcionais ao executar uma fatia: list[start:end], por exemplo:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
 
# 5. Você pode excluir fatias usando a instrução del:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
 
del my_list[:]
print(my_list)  # deletes the list content, outputs: []
 
# 6. Você pode testar se alguns itens existem em uma lista ou não estão usando as palavras-chave in e not in, por exemplo:
my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
 
############################
### 3.6.8 TESTE DA SEÇÃO ###
############################

# Pergunta 1: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0]
 
print(list_3)
# Saída: ['C']

# Pergunta 2: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2
 
print(list_3)
# Saída: ['B', 'C']

# Pergunta 3: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[:]
 
print(list_3)
# Saída: [ ]

# Pergunta 4: Qual é a saída do trecho de código?
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
 
del list_1[0]
del list_2[0]
 
print(list_3)
# Saída: ['A', 'B', 'C']


# Pergunta 5: Insira in ou not in ao invés de ??? para que o código produz o resultado esperado.
my_list = [1, 2, "in", True, "ABC"]
 
print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False