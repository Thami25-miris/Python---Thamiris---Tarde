# Crie lista vazia chamada turma
#imprima a lista
#adicione os nomes Monica, Magali e Chico Bento
#imprima lista
#Peça ao usuário para digitar nomes a lista (Cebolinh e Casção) - Use Loop FOR
#Impima a lista
#Remova Cebolinha e Casção da lista
#Imprima a lista
# Adiciona Sansão no inicio da lista
#Imprima a lista
# Imprima: "Essa turma tem (comprimnto da lista) membros"


turma = []
print(turma)

turma.append("Monica")
turma.append("Magali")
turma.append("Chico Bento")
print(turma)

for i in range(2):
    turma.append(input("Digite nome: "))
print(turma)

del turma [4]
del turma [3]
print(turma)

turma.insert(0, "Sansão")
print(turma)

print("Essa turma tem", len(turma),"membros")