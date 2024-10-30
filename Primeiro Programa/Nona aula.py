# Hipótese de Collatz - Todo número inteiro positivo coverge para 1
#Digite um número inteiro
#Se o numero = 0, print "Número deve ser diferente de zero"
#Se PAR, divida por 2
#Se IMPAR, multiplique por 3 e some 1 (x*3+1)
#Imprima o resultado
#Conte a quantidade de Loops
#Se permanecer diferente de 1, repita a operção
#Imprima a quantidade total de etapas

numero= int(input("Digite um número inteiro: "))
etapas = 0

if numero == 0:
    print("Número deve ser difeente de zero")
else:
    while numero != 1:
         if numero % 2 == 0:
            numero //= 2
         else:
             numero = numero*3+1
         print(numero)
         etapas += 1
print("Etapas: ", etapas)


