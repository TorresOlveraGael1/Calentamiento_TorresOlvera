#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

print(" ")
print("Torres Olvera Gael")
print(" ")

def es_vocal(caracter):
    #Convertir el carácter a minúscula para facilitar la comparación
    caracter = caracter.lower()
    #Comprobar si el carácter es una vocal
    return caracter in 'aeiou'

#Solicitar al usuario que ingrese un carácter
caracter_usuario = input("Ingresa un carácter: ")

#Verificar si el carácter ingresado es una vocal
if len(caracter_usuario) == 1:  #Asegurarse de que solo se ingrese un carácter
    resultado = es_vocal(caracter_usuario)
    print(f"¿El carácter '{caracter_usuario}' es una vocal? {resultado}")
else:
    print("Por favor, ingresa solo un carácter.")