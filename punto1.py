#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

print(" ")
print("Torres Olvera Gael")
print(" ")

#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

#Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

#Llamar a la función max() con los números ingresados
resultado = max(numero1, numero2)

#Mostrar el resultado
print("El mayor es:", resultado)