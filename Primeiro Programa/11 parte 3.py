#Registro de temperatura 
# 1 registro por hora
# 31 dia do mês
# 24 * 31 = 744 valores por mês
#Coluna: horas (24 colunas)
#Linhas: 31 dias

temp = [[0.0 for i in range(24)] for j in range(31)]

for i in range(31):
    temp[i][12] = 33.3

for linha in temp:
    print(linha)

total = 0.0
for dias in temp:
    total += dias [12]
print(total)
media=total/31
print("Temperatura média mensal do meio dia: ", media)

dias_quentes = 0
for dias in temp:
    if dias[12] > 20.0:
        dias_quentes+=1

print(dias_quentes, "dias estavam quentes")