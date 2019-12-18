#6Pide una cadena por teclado, mete los caracteres en una lista sin espacios.


bandera = True
x= []
intentos = 5
while intentos != 0 :
    palabra = (input('Ingrese caracteres sin espacio: '))
    x.append(palabra)
    intentos = intentos -1
    print("Te quedan: ", intentos, "intentos")
print (x)

