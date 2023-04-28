# 3.2.15 LAB - A hipótese de Collatz

# Cenário

# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:

# 1 - pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
# 2 - se for par, avalie um novo c0 como c0 ÷ 2;
# 3 - caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# 4 - se c0 ≠ 1 , volte ao ponto 2.

# A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.

# Obviamente, é uma tarefa extremamente complexa usar um computador para provar a hipótese de qualquer número natural (pode até exigir inteligência artificial), 
# mas você pode usar o Python para verificar alguns números individuais. Talvez você até encontre aquele que refutaria a hipótese.

# Escreva um programa que leia um número natural e execute as etapas acima, desde que c0 permaneça diferente de 1. 
# Também queremos que você conte as etapas necessárias para atingir o objetivo. Seu código deve gerar todos os valores intermediários de c0 também.

# Dica: a parte mais importante do problema é como transformar a ideia de Collatz em um loop while - essa é a chave para o sucesso.

# Teste seu código usando os dados que fornecemos.

numero = int(input("Digite um número natural: "))
contador = 0
while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
    contador += 1
print(numero)
print("Número de etapas:", contador)

