#Definir una función que calcule la longitud de una lista o una cadena dada.

print(" ")
print("Torres Olvera Gael")
print(" ")

def calcular_longitud(elemento):
    return len(elemento)

# Solicitar al usuario que ingrese una cadena o una lista
entrada = input("Ingrese una cadena o una lista (separando los elementos por comas si es una lista): ")

# Verificar si la entrada es una lista o una cadena
if entrada.startswith("[") and entrada.endswith("]"):
    # Convertir la entrada en una lista
    lista = eval(entrada)  # Usar eval con precaución, solo en entornos controlados
    longitud = calcular_longitud(lista)
else:
    # Considerar que es una cadena
    longitud = calcular_longitud(entrada)

print(f"La longitud es: {longitud}")