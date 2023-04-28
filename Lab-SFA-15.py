# 3.2.11   LAB   A declaração continue – o Belo Comedor de Vogais
#
# Cenário:
#
# Sua tarefa aqui é ainda mais especial do que antes: você deve reprojetar o (feio) comedor de vogal do laboratório anterior e criar um melhor (bonito) 
# comedor de vogal! Escreva um programa que use:
#
# um loop for
# o conceito de execução condicional (if-elif-else)
# a declaração continue.
#
#
# Seu programa deve:
#
# 1 - peça ao usuário para inserir uma palavra;
# 2 - use user_word = user_word.upper() para converter em maiúsculas a palavra inserida pelo usuário; 
#       falaremos sobre métodos de string e o método upper() muito em breve - não se preocupe;
# 3 - use execução condicional e a declaração continue para "consumir" as seguintes vogais A, E, I, O, U da palavra inserida;
# 4 - atribua as letras não consumidas à variável word_without_vowels e imprima a variável na tela.
# Veja o código no editor. Criamos word_without_vowels e atribuímos uma string vazia a ela. Use a operação de concatenação para pedir ao Python que combine letras 
# selecionadas em uma sequência mais longa durante as voltas de loop subsequentes e atribua-a à variável word_without_vowels.

# Teste seu programa com os dados que fornecemos para você.

# Solicitar ao usuário que digite uma palavra
# e atribua-o à variável user_word.

user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)