#Exemplos listas + FOR

quadrados = [x **2 for x in range (10)]  #Considerando x de 0 a 10 e elevar ao quadrado
print(quadrados)

potenciacao = [ 2**i for i in range (8)]  # o i vai ser de 0 a 8, ou seja, vai ser 2 elevado a i 
print(potenciacao)

lista = [1,2,3,4,5,6,7,8,9]
impar = [x for x in lista if x%2 != 0]
print(impar)