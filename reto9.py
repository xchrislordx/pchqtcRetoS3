#Crea una lista con números e indica el numero con mayor valor y el que menor tenga

bandera = True
valor = []
while bandera == True:
    numero = int(input("Ingrese numero: "))
    valor.append(numero)
    if numero == 0:
        bandera = False

print("El valor maximo es el ",max(valor))
print("El valor minimo es el ",min(valor))