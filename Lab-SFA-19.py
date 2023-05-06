# 3.4.11   LAB   O básico de listas ‒ os Beatles

# Cenário
# Os Beatles foram um dos grupos de música mais populares dos anos 60, e a banda mais vendida na história. 
# Algumas pessoas consideram que eles são o ato mais influente da era do rock.
# Na verdade, eles foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.

# A banda passou por muitas mudanças na formação, culminando em 1962 com a formação de John Lennon, Paul McCartney, George Harrison e Richard Starkey (mais conhecido como Ringo Starr).

# Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:


# etapa 1: criar uma lista vazia chamada beatles;
beatles = []
print("Etapa 1:", beatles)

# etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
beatles.append ("John Lennon")
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")
print("Etapa 2:", beatles)

# etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
for i in range(1):
    beatles.append ("Stu Sutcliffe")
    beatles.append ("Pete Best")
print("Etapa 3:", beatles)

# etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
del beatles[4]
del beatles[3]
print("Etapa 4:", beatles)

# etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

# A propósito, você é um fã dos Beatles? (Os Beatles são uma das bandas favoritas de Greg. Mas espere ... quem é Greg ...?)
print("o fabuloso", len(beatles))

