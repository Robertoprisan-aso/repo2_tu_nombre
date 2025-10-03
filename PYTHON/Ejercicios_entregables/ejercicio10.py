trabajoFinal = float(input("Tu nota del trabajo final: "))
examenFinal = float(input("Tu nota del examen final: "))
calificacionParcial1 = float(input("Cal.1: "))
calificacionParcial2 = float(input("Cal.2: "))
calificacionParcial3 = float(input("Cal.3: "))

promedioParcialFinal = ((calificacionParcial1 + calificacionParcial2 + calificacionParcial3)/ 3) * 0.55
examenFinalFinal = (examenFinal) * 0.30
trabajofinalFinal = (trabajoFinal) * 0.15

notaFinal = promedioParcialFinal + examenFinalFinal + trabajofinalFinal


print(str(notaFinal))