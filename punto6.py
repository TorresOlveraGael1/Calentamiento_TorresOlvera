#Definir una función inversa() que calcule la inversión de una cadena

print(" ")
print("Torres Olvera Gael")
print(" ")

def inversa(cadena):
    return cadena[::-1]

#Solicitar al usuario que ingrese una cadena
cadena_usuario = input("Ingrese una cadena: ")
cadena_invertida = inversa(cadena_usuario)

print("Cadena invertida:", cadena_invertida)