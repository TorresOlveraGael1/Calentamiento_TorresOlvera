#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.

print(" ")
print("Torres Olvera Gael")
print(" ")

def sum(lista):
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    total = 1
    for num in lista:
        total *= num
    return total

#Solicitar al usuario que ingrese los números
entrada = input("Introduce los números separados por comas: ")
#Convertir la entrada en una lista de números
numeros = [int(num) for num in entrada.split(',')]

#Calcular la suma y la multiplicación
resultado_suma = sum(numeros)
resultado_multiplicacion = multip(numeros)

#Mostrar los resultados
print("La suma de los números es:", resultado_suma)
print("La multiplicación de los números es:", resultado_multiplicacion)