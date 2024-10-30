# Método items(): retorna tuplas, cada tupla é um par key-value


dicionario = {"gato":"chat","cachorro":"chien","cavalo":"cheval"}

for portugues, frances in dicionario.items():
    print(portugues,"=",frances)