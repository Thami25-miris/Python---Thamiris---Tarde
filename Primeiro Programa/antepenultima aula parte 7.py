def minha_funcao(n):
    print("Eu obtive: ", n)
    n+=1
    print("Agora tenho: ",n)
    var = n
    print("Dentro da função: ",var)

var = 1
minha_funcao(var)
print("Fora da função: ",var)