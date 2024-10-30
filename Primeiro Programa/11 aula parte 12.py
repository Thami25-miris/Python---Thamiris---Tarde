#Funções com 3 parâmetros:

def endereco(rua, cidade,cep):
    print("Seu endereço é rua ", rua,"na cidade de",cidade,"-CEP",cep)

r = input("Rua: ")
c = input("Cidade: ")
cp = input("Cep: ")

endereco(r,c,cp)