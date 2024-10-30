# Identificação do maior elemento

lista = [7,3,11,5,1,9,7,15,13]
maior = lista[0]                  # adotou-se que o maior elemento da lista é o que está na posição 0

for i in range (1,len(lista)):    #considere a partir da posição 1, e todos os elementos precisam ser comparados com caso abaixo
    if lista[1] > maior:          
        maior = lista[i]

print(maior)


# Outra forma de fazer o mesmo case acima:


# lista = [7,3,11,5,1,9,7,15,13]
# maior = lista[0]                  

#for i in lista  
    #if i > maior:          
        #maior = i

#print(i)
