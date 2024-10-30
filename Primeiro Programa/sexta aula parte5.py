var = int(input("Digite um número: "))
if var >= 20:
    print("Seu número é maior ou igual a 20")
    if var <= 100:
        print("é menor ou igual a 100")
    else:
        print("é maior que 100")  
else:
    if var < 10:
        print("seu número é menor que 10")
    else:
        print("Seu número é maior que 10 e menor que 20")