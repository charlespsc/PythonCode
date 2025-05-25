########################################################
### 4.3.7   LAB   Números primos ‒ como encontrá-los ###
########################################################

# Um número natural é primo se for maior que 1 e não tiver divisores diferentes de 1 e ele próprio.

# Complicado? Não mesmo. Por exemplo, 8 não é um número primo, pois você pode dividi-lo por 2 e 4 
# (não podemos usar divisores iguais a 1 e 8, pois a definição proíbe isso).

# Por outro lado, 7 é um número primo, pois não podemos encontrar divisores legais para ele.

# Sua tarefa é escrever uma função verificando se um número é primo ou não.

# A função:

# é chamado is_prime;
# requer um argumento (o valor a ser verificado)
# retorna True se o argumento for um número primo e False caso contrário.
# Dica: tente dividir o argumento por todos os valores subsequentes (começando em 2)
# e verifique o restante - se for zero, seu número não pode ser um primo; 
# pense bem quando deve interromper o processo.

# Se você precisar conhecer a raiz quadrada de qualquer valor, poderá utilizar o operador **.
#  Lembre-se: a raiz quadrada de x é o mesmo que x0.5

# Preencha o código no editor.
# Execute o código e verifique se a saída é igual à nossa.
# Saída prevista: 2 3 5 7 11 13 17 19

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): # Adicionado +1 para incluir a raiz quadrada
        if num % i == 0:
            return False  # Se for divisível por algum número, não é primo
    return True  # Se não encontrou nenhum divisor, é primo

# Loop para testar números de 1 a 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
