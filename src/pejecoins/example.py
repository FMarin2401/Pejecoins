import __init__ as test

while True: #Bucle para realizar varias prubas con control
    usuario = str(input("Prueba: "))

    if usuario == "suma":
        resultado = test.suma(2,3)
        print(resultado)
         
    elif usuario == "MxM":
        a = [[-1, 0, 1], [7, (3/2), -(13/2)], [3, (1/2), -(5/2)]]
        b = [[11],[-4], [10]]

        resultado = test.multmat(a, b)
        
    else:
        print("Comando Equivocado. Intenta de nuevo.")