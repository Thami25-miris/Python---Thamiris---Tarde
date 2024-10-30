#Desafio
x = input("Digite 'M' para sistema métrico ou 'I' para sistema imperial: ")
def libras_to_kilos (x):
    Kilos = x*0.453592
    return Kilos
def pes_to_metros(y):
    metros = y * 0.3048
    return metros
def imc (peso,altura):
    imc = round(peso/altura**2,2)
    if imc<18.5:
        print("Seu IMC é",imc,"Classificação: magreza")
    elif imc>=18.5 and imc<24.9:
        print("Seu imc é", imc,"Classificação: normal")
    elif imc>= 25 and imc<=29.9:
        print("Seu imc é",imc, "Classificação: sobrepeso")
    elif imc>=30 and imc <= 39.9:
        print("Seu imc é",imc,"Classificação: Obesidade")
    else:
        print("Seu imc é",imc,"Classificação: Obesidade grave")

if x== "I":
    peso = libras_to_kilos(float(input("Digite seu peso em libras: ")))
    altura = pes_to_metros(float(input("Digite sua altura em pés: ")))
    imc(peso,altura)
else:
    peso = float(input("Digite seu peso em Kilos: "))
    altura = float(input("Digite sua altura em metros: "))
    imc(peso,altura)

             