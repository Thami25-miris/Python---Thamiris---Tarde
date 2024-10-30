# Identificação da localização do elemento

lista = [1,2,3,4,5,6,7,8,9,10]
encontrar = 5
finalizando = False

for i in lista:
    finalizando = lista[i] == encontrar
    if finalizando:
        break

if finalizando:
    print("Elemento encontrado no índice: ", i)
else:
    print("Elemento não encontrado")