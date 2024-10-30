minha_lista= [1,None,True, "Senai", 256,0]

print(minha_lista[3])      # Estou pedindo para me trazer o elemento localizado na posição 3, lembrando que contamos a partir de 0
print(minha_lista[-1])     #Com sinal de negaivo a contagem fica da direita para esquerda 
minha_lista[1]= "Maua"
minha_lista.insert(0,"primeiro")
minha_lista.append("último")
print(minha_lista)