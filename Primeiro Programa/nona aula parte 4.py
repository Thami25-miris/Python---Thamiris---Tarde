# Opeador Lógico - Not
# testar 0, 1, 34 e 5
# print(not(A>0)) - o Not na frete da operação : SIGNIFICA IMPRIME O INVERSO DO RESULTADO

A = int(input("Digite valor A: "))


if A:
    print("0 - False")
else:
    print("1 - True")

print(A>0)
print(not(A>0))
print(A!=0)
print(not(A==0))
y = not A
print(y)
z = not not A
print(z)