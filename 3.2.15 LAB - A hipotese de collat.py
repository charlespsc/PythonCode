# 3.2.15   LAB   A hipótese de Collat

# Cenário
# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não comprovada) que pode ser descrita da seguinte forma:

# 1. pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
# 2. se for par, avalie um novo c0 como c0 ÷ 2;
# 3. caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# 4. se c0 ≠ 1 , volte ao ponto 2.

# A hipótese diz que, independentemente do valor inicial de c0, ela sempre vai para 1.

# Obviamente, é uma tarefa extremamente complexa usar um computador para provar a hipótese de qualquer número natural (pode até exigir inteligência artificial),
#  mas você pode usar o Python para verificar alguns números individuais. Talvez você até encontre aquele que refutaria a hipótese.

# Escreva um programa que leia um número natural e execute as etapas acima, desde que c0 permaneça diferente de 1. 
# Também queremos que você conte as etapas necessárias para atingir o objetivo. Seu código deve gerar todos os valores intermediários de c0 também.

# Dica: a parte mais importante do problema é como transformar a ideia de Collatz em um loop while - essa é a chave para o sucesso.

# Teste seu código usando os dados que fornecemos.

# Código feito pelo copilot.
# Solicita ao usuário que insira um número natural
c0 = int(input("Digite um número natural: "))
# Inicializa o contador de etapas
steps = 0
# Enquanto c0 for diferente de 1
while c0 != 1:
    # Se c0 for par, divide por 2
    if c0 % 2 == 0:
        c0 = c0 // 2
    # Caso contrário, se c0 for ímpar, calcula 3 * c0 + 1
    else:
        c0 = 3 * c0 + 1
    # Incrementa o contador de etapas
    steps += 1
    # Imprime o valor atual de c0
    print(c0)
# Imprime o número total de etapas
print("Número total de etapas:", steps)     
# A saída do programa deve ser semelhante a esta:
# Digite um número natural: 5
# 16
# 8         
# 4
# 2
# 1
# Número total de etapas: 5