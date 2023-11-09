import __init__ as test

print("""
Que prueba va a realizar:
-----
1) Suma => suma
2) Multiplicacion de matrices => MxM
3) Multiplicacion de matriz por vector => MxV
-----
      
""")


while True: #Bucle para realizar varias prubas con control
    
    usuario = str(input("Prueba: "))

    if usuario == "suma":
        resultado = test.suma(2,3)
        print(resultado)
         
    elif usuario == "MxM":
        a = [[-1, 0, 1], [7, (3/2), -(13/2)], [3, (1/2), -(5/2)]]
        b = [[11],[-4], [10]]

        resultado = test.multMat(a, b)
    elif usuario == "MxV":
        a = [[-1, 0, 3, 4], [7, 3, 5, 6], [3, 2, 4, 3]]
        b = 2
        resultado = test.multVector(a,b)
        
        
    else:
        print("Comando Equivocado. Intenta de nuevo.")