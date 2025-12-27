# Calculadora básica en Python

print("Bienvenido a la calculadora")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("Elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Selecciona una opción (1/2/3/4): ")

if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Error: no se puede dividir entre cero")

else:
    print("Opción no válida")
 print("\nPresiona ENTER para continuar")
    print("Escribe ESC y presiona ENTER para salir")

    salir = input(">> ").lower()

    if salir == "esc":
        print("Gracias por usar la calculadora 👋")
        break
