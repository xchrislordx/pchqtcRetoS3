#4) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar.
#Por último, muestra los números ordenados de menor a mayor.

bandera = True
valor = []
while bandera == True:
    numero = int(input("Ingrese numero: "))
    valor.append(numero)
    if numero == 0:
       bandera = False
valor.sort()
print(valor)
