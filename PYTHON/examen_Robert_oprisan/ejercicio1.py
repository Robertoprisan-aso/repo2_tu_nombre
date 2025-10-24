#Ejercicio1: 


peso = int(input("Dame un peso entre 50-100 kg: ")) 
altura = float(input("dame una altura entre 1.50-2.00M: ")) 
formula_IMC = peso / altura**2

print(round(formula_IMC,1))
