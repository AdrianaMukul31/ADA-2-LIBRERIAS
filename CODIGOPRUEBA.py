from ordenamiento.numeros_insercion import insercion
def pedirnumeros():
    while True:
        try:
            tamano=int(input("Cuantos numeros requieres ordenar?"))
            if tamano>0:
                break
            else:
                print("ingrese un numero valido")
        except ValueError:
            print("introduce un numero entero")
    lista=[]
    print("Introduce los numeros para ordenar:")
    for _ in range(tamano):
        while True:
            try:
                elemento= int(input("elemento:"))
                lista.append(elemento)
                break
            except ValueError:
                print("ingresa un numero valido")
    return lista
lista= pedirnumeros()
print(f"lista original:{lista}")
lista_ordenada= insercion(lista)
print(f"lista ordenada: {lista_ordenada}")
