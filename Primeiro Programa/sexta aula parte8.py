var = int(input("Digite o primeiro número: "))
var2 = int(input("Digite o segundo número: "))
var3 = int(input("Digite o terceiro número: "))

if var > var2:
    print("O maior número foi: ", var)
elif var < var2:
    print("O maior número foi: ", var2)
elif var2 > var3:
    print("O maior número foi: ", var2)
else:
     print("O maior número foi: ",var3)