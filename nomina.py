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

        if len(empleados) == 0:
            print("No hay empleados registrados")

    else:

        for empleado in empleados:

            salario_base = empleado["salario"]
            dias = empleado["dias"]

            salario_dias = (salario_base / 30) * dias

            auxilio = 0

            if salario_base < 2600000:
                auxilio = 160000

                descuento = salario_dias * 0.08

                total_pagar = salario_dias + auxilio - descuento

                print("\n===== DESPRENDIBLE =====")
                print("Empleado:", empleado["nombre"])
                print("Salario por días:", salario_dias)
                print("Auxilio:", auxilio)
                print("Descuento:", descuento)
                print("Total a pagar:", total_pagar)

            elif opcion == "3":

                print("Saliendo del sistema...")
                break

            else:
             print("Opción inválida")