#Ejercicio2

segundos = int(input("Dime una cantidad de segundos entre 0-10000: "))

h = segundos // 3600
min = (segundos % 3600) // 60
seg_que_faltan = segundos % 60

print("horas: " + str(h) + " minutos: " + str(min) + " segundos: "+ str(seg_que_faltan))