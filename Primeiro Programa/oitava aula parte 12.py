# Soma de um intervalo de números

numero = int(input(" Digite o número inicial: "))
numero2 = int(input("Digite o número final: "))
soma=0

for numero in range(numero,numero2):
    soma += numero
    print(soma)
    
    