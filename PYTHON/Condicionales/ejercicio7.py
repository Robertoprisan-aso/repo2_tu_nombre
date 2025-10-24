import math
base = int(input("introduce una base: "))
exponente= int(input("introduce un exponente: "))

if exponente > 0:
    potencia = base ** exponente
    print("Exponente positivo: " + str(potencia))
if exponente == 0:
    print(potencia)
if exponente < 0:
    potencia1 = base ** abs(exponente)
    resultado = 1/potencia1
    print("El resultado es: " + str(resultado))



    