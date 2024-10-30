# TRY e EXCEPT
while True:
    try:
        valor = int(input("Digite um número: "))
        print("Resultado",1/valor)
        break
    except (ValueError,ZeroDivisionError):
        print("Tipo errado")
    except:
        print("Alguma outra exceção")