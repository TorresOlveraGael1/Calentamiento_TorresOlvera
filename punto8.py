#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

print(" ")
print("Torres Olvera Gael")
print(" ")

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

#Solicitar al usuario que ingrese las dos listas
lista1 = input("Ingresa los elementos de la primera lista separados por comas: ").split(",")
lista2 = input("Ingresa los elementos de la segunda lista separados por comas: ").split(",")

#Llamar a la función y mostrar el resultado
resultado = superposicion(lista1, lista2)
print("¿Las listas tienen al menos un miembro en común?", resultado)