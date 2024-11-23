#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

print(" ")
print("Torres Olvera Gael")
print(" ")

def procedimiento():
    #Solicitar al usuario que ingrese números enteros separados por espacios
    entrada = input("Ingrese una lista de números enteros separados por espacios: ")
    
    #Convertir la entrada en una lista de enteros
    numeros = list(map(int, entrada.split()))
    
    #Imprimir el histograma
    print("Histograma:")
    for numero in numeros:
        #Imprimir el número seguido de '*' según su valor
        print(f"{numero}: {'*' * numero}")

#Llamar al procedimiento
procedimiento()