#Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.

bandera = True
x= []
intentos = 5
while intentos != 0 :
    palabra = (input('Ingrese caracteres: '))
    x.append(palabra)
    intentos = intentos -1
    print("Te quedan: ", intentos, "intentos")
y=set(x)
print (y)

