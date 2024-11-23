#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.

print(" ")
print("Torres Olvera Gael")
print(" ")

def generar_n_caracteres():
    #Solicitar al usuario que ingrese un número entero
    n = int(input("Ingresa un número entero: "))
    #Solicitar al usuario que ingrese un carácter
    caracter = input("Ingresa un carácter: ")
    
    #Devolver el carácter multiplicado por el número
    return caracter * n

#Llamar a la función y mostrar el resultado
resultado = generar_n_caracteres()
print(resultado)