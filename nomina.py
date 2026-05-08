empleados = []

while True:

    print("\n===== SISTEMA DE NÓMINA =====")
    print("1. Registrar empleado")
    print("2. Calcular nómina")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Ingrese el nombre del empleado: ")
        salario = float(input("Ingrese salario base: "))
        dias = int(input("Ingrese días trabajados: "))

        empleado = {
            "nombre": nombre,
            "salario": salario,
            "dias": dias
        }

        empleados.append(empleado)

        print("Empleado registrado correctamente")

    elif opcion == "2":

        print("Función en desarrollo...")

    elif opcion == "3":

        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")