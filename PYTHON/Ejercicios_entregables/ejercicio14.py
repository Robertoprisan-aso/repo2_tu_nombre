num = int(input("introduce el num: "))


decena = num // 10
unidad = num % 10


numFinal = unidad * 10 + decena


print("EL numero invertido es: "+ str(numFinal))