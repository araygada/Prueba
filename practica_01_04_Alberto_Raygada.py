# Ejercicio 1.4 - Alberto Raygada
# Escriba un programa que solicite dos números, verifique que el primero es estrictamente
# menor que el segundo y calcula la suma de todos los números impares que se encuentran
# entre el primero número y el segundo número.
# -------------------------------------------------------------------------------------------------------------------------

inicio:

mensaje = "Se le va a solictar que ingrese dos números para conformar un rango y "
mensaje = mensaje + "listar los números impares dentro del mismo."
print(mensaje)

num1 = int(input("Incluya el primer numero del rango: "))
num2 = int(input("Incluya el segundo numero del rango: "))

if num1 < num2:
    suma = [i for i in range(num1, num2) if (i%2!=0)]
    print(suma)
else:
    mensaje = "El primer número incluido debe ser menor al segundo. Intente de nuevo."
    print(mensaje)
    goto inicio




