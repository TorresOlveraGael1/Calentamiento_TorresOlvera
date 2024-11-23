#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

print(" ")
print("Torres Olvera Gael")
print(" ")

#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    
    if num2 > num1 and num2 > num3:
        return num2
    
    if num3 > num1 and num3 > num2:
        return num3

#Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

#Llamar a la función max() con los números ingresados
resultado = max(numero1, numero2, numero3)

#Mostrar el resultado
print("El mayor es:", resultado)