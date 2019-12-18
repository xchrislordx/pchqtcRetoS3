def contarElementosLista(lista):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    return {i:lista.count(i) for i in lista}
lista = []
bandera = True
while bandera == True:
    numero = int(input("Ingrese numero: "))
    lista.append(numero)
    if numero == 0:
       bandera = False
resultado=contarElementosLista(lista)
maximo=max(resultado, key=resultado.get)
print("El valor mas repetido es el ",maximo," con ",resultado[maximo]," veces")