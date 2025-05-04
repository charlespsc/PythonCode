# 3.2.9 LAB A declaração break – Preso em um loop

# Cenário: 
# A declaração break é usada para sair/encerrar um loop.

# Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra, a menos que o usuário insira "chupacabra" 
# como a palavra de saída secreta, caso em que a mensagem "Você saiu do loop com sucesso". Deve ser impresso na tela, e o loop deve terminar.

# Não imprima nenhuma das palavras inseridas pelo usuário. Use o conceito de execução condicional e a declaração break.

# código feito pelo copilot.   
while True:
    palavra = input("Digite uma palavra ou 'chupacabra' para sair: ")
    if palavra == "chupacabra":
        print("Você saiu do loop com sucesso.")
        break
        #Não imprima nada se a palavra não for "chupacabra"

