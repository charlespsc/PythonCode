# # 3.2.9   LAB   A declaração break – Preso em um loop
# # #Cenário
# # A declaração break é usada para sair/encerrar um loop.

# # Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra, a menos que o usuário insira "chupacabra" 
# # como a palavra de saída secreta, caso em que a mensagem "Você saiu do loop com sucesso". 
# # Deve ser impresso na tela, e o loop deve terminar.

# # Não imprima nenhuma das palavras inseridas pelo usuário. 
# # Use o conceito de execução condicional e a declaração break.


# # --------------------------------------------------------------------------------------------------------------------------------
# print("\n ### The break instrução: ###")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Dentro do laço.", i)
# print("Fora do loop.")


secret = "chupacabra"

# Solicitando o nome.
name = input("Digite a palavra secreta:")
#
# Verificar se o número inserido pelo usuário é igual ao número escolhido pelo mágico. 
while name != secret:
    if name == secret:
        break
    print("Digite a palavra secreta para sair do loop! \n")
    name = input("Digite a palavra secreta:")
print("Você saiu do loop com sucesso!")
