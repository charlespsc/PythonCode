#LAB   Trabalhando com a função print()
# 
# Cenário
#O comando print(), que é uma das diretrizes mais fáceis em Python, simplesmente imprime uma linha na tela.
#
#Em seu primeiro laboratório:
#
# 1 - Use a função de print() para imprimir a linha Olá, Python! na tela. Use aspas duplas ao redor da string.
# 2 - Depois de fazer isso, use a função print() novamente, mas desta vez imprima seu primeiro nome.
# 3 - Remova as aspas duplas e execute o código. Assista à reação do Python. Que tipo de erro é gerado?
    # Traceback (most recent call last):
    #   File "/home/charles/Documentos/GitHub/PythonCode/LAB-1", line 22, in <module>
    #     print(Charles)
    # NameError: name 'Charles' is not defined
#
# 4 - Em seguida, remova os parênteses, coloque aspas duplas e execute o código novamente. Que tipo de erro é gerado desta vez?
    #   File "/home/charles/Documentos/GitHub/PythonCode/LAB-1", line 23
    #        print "Charles"
    #        ^^^^^^^^^^^^^^^
    # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#
# 5 - Experimente o máximo que puder. Altere aspas duplas para aspas simples, use várias funções print() na mesma linha e, em seguida, em linhas diferentes. 
#
#Veja o que acontece.

print ("Olá, Python")
# print (Charles) -> retirar o comentário para gerar o erro!
# print "Charles" -> retirar o comentário para gerar o erro!
print ('Charles')
print ("teste")
print()
print("A pequenina aranha escalou a tromba d'água.")
print()
print("Caiu a chuva e lavou a aranha.")
print()
print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")

# print("\")
#      print("\")
#            ^
# SyntaxError: unterminated string literal (detected at line 38)
print()
print("\\")
print()
print("A aranha pequenininha" , "subiu" , "a tromba d'água.") # 3 argumentos
print()
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")
print()
print("Meu", "nome", "é", "Monty", "Python.", sep="->")
print()
print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print()
# Solução de Amostra

print("Olá, Python!")
# print("Greg")
# print(Greg)
# print"Greg"
# print('Greg')
# print("Greg") print("Python")
# ...</sampleSolution>
