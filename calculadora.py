input("Presiona ENTER para iniciar la calculadora...")

print("Bienvenido a la calculadora")

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: solo puedes ingresar números.")
        continue

    print("\nElige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == "1":
        resultado = num1 + num2

    elif opcion == "2":
        resultado = num1 - num2

    elif opcion == "3":
        resultado = num1 * num2

    elif opcion == "4":
        if num2 == 0:
            print("Error: no se puede dividir entre cero")
            continue
        resultado = num1 / num2

    else:
        print("Opción no válida")
        continue

    print("Resultado:", resultado)

    print("\nENTER para continuar | escribe ESC para salir")
    salir = input(">> ").lower()

    if salir == "esc":
        print("Gracias por usar la calculadora 👋")
        break
