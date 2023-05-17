
#########################################################################
#### 4.3.4   LAB   Um ano bissexto: escrevendo suas próprias funções ####
#########################################################################

# Sua tarefa é escrever e testar uma função que usa um argumento (um ano) e retorna True se o ano for um ano bissexto ou False caso contrário.
# A semente da função já é semeada no código de esqueleto no editor.

# Nota: também preparamos um código de teste curto, que você pode usar para testar sua função.

# O código usa duas listas - uma com os dados de teste e a outra contendo os resultados esperados. O código informará se algum dos resultados é inválido.

def eh_ano_bissexto(ano):
    if ano % 4 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 400 == 0:
        return True
    else:
        return True

test_data = [1900, 2000, 2016, 1987]

test_results = [False, True, True, False]
for i in range(len(test_data)):
 ano = test_data[i]
 print(ano,"-> ",end="")
 result = eh_ano_bissexto(ano)
 if result == test_results[i]:
    print("OK")
 else:
    print("Fracassado")
    
    
### Outra forma de fazer
    
def eh_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(eh_ano_bissexto(1900))  
print(eh_ano_bissexto(2000)) 
print(eh_ano_bissexto(2016))
print(eh_ano_bissexto(1987))  

# Outra forma:

ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')