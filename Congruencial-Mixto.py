cant = int (raw_input("Cantidad de numeros a generar "))
c = int (raw_input("Constante aditiva "))
a = int (raw_input("Constante multiplicativa "))
semilla= int (raw_input("Ingrese la semilla "))
n = int (raw_input("Ingrese el modulo "))

print " "
for i in range (cant):
    i += 1
    xn = ((a*semilla)+c)%n    
    z = float((xn+.0) / (n+.0))
    print (xn, z)
    semilla = xn
