# Diferença entre DEL e CLEAR

dicionario = {"gato":"chat","cachorro":"chien","cavalo":"cheval"}
print(len(dicionario))

del dicionario["gato"]
print(len(dicionario))

dicionario.clear()
print(len(dicionario))

del dicionario