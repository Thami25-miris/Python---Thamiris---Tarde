#Loteria

resultado = [5,11,9,42,3,49]
aposta = [5,7,11,42,34,49]
acertos = 0

for i in aposta:
    if i in resultado:
        acertos += 1

print("Você acertou: ", acertos,"números")