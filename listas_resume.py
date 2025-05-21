# 1. A lista é um tipo de dados em Python usado para armazenar vários objetos. 
#    É uma coleção ordenada e mutável de itens separados por vírgula entre colchetes, por exemplo:
my_list = [1, None, True, "eu sou um barbante", 256, 0]
print(my_list)

# 2. As listas podem ser indexadas e atualizadas, por exemplo:
my_list = [1, None, True, 'eu sou um barbante', 256, 0]
print(my_list[3])  # outputs: eu sou um barbante
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'eu sou um barbante', 256, 0]
 
my_list.insert(0, "primeiro")
my_list.append("último")
print(my_list)  # outputs: ['primeiro', 1, '?', True, 'eu sou um barbante', 256, 0, 'último']
 

# 3. As listas podem ser aninhadas, por exemplo:
my_list = [1, 'a', ["lista", 64, [0, 1], False]]
 
# 4. Os elementos e as listas podem ser excluídos, por exemplo:
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
 
del my_list  # exclui toda a lista


# 5. As listas podem ser iteradas usando o loop for, por exemplo:
my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
 
for color in my_list:
    print(color)
 
# 6. A função len() pode ser usada para verificar o comprimento da lista, por exemplo:
my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
print(len(my_list))  # outputs 5
 
del my_list[2]
print(len(my_list))  # outputs 4
print(my_list)  # outputs ['branco', 'roxo', 'amarelo', 'verde']

 
# 7. Uma chamada de função típica tem a seguinte aparência: 
#   result = function(arg)  ->  enquanto uma chamada de método típico se parece com isso: 
#   result = data.method(arg)

## 3.4.13 TESTE DA SEÇÃO ##

# Pergunta 1: Qual é a saída do trecho de código?
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
 
print(lst)
 
# Pergunta 2: Qual é a saída do trecho de código?
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
 
for number in lst:
    add += number
    lst_2.append(add)
 
print(lst_2)
 
# Pergunta 3: Qual é a saída do trecho de código?
lst = []
del lst
print(lst)
 
## saída: NameError: name 'lst' is not defined


# Pergunta 4: Qual é a saída do trecho de código?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
 
