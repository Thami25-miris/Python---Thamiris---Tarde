#Fatiamento de lista - índices negativos

minha_lista =[10,8,6,2,4]
nova_lista = minha_lista[1:-1]                   # do elementro 1 ao 4, mas o 4 não entra
print(nova_lista)

minha_lista =[10,8,6,2,4]
nova_lista = minha_lista[- 1:1]           
print(nova_lista)


minha_lista =[10,8,6,2,4]
nova_lista = minha_lista[: 3]
print(nova_lista)



minha_lista =[10,8,6,2,4]
nova_lista = minha_lista[3:]
print(nova_lista)

minha_lista =[10,8,6,2,4]
nova_lista = minha_lista[:]  # considera todos os elementos da lista
print(nova_lista)