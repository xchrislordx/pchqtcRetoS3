#mj1 = [2, 4, 4, 4, 4, 4, 9, 9]
#mj2 = set(mj1)

#set([9, 2, 4])
#list(mj2)
#sorted(list(mj2))
#print(mj2)

#string = 'Hola    mundo'
#print(string.replace(' ', ''))

#print (veces = ['a','b','a'].count('a'))
cadenaPalabras = int(input("Ingrese numero: "))

listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))