
inicio = int(input("\nDigite o número inicial: "))
fim = int(input("Digite o número final: "))
final = fim + 1
soma = 0

for i in range(inicio,final):
    soma += i

print("\nA soma dos números de", inicio,"a", fim,"é", soma,"\n")