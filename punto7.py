#Definir una función es_palindromo() que reconoce palíndromos

print(" ")
print("Torres Olvera Gael")
print(" ")

def es_palindromo():
    #Pedir al usuario que ingrese una cadena
    cadena = input("Introduce una cadena: ")
    
    #Normalizar la cadena
    cadena_normalizada = ''.join(cadena.split()).lower()  #Eliminar espacios y convertir a minúsculas
    
    #Verificar si la cadena es igual a su reverso
    if cadena_normalizada == cadena_normalizada[::-1]:
        return True
    else:
        return False

#Ejemplo de uso
if es_palindromo():
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")