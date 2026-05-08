from calculos import calcular_nomina

empleados = []

while True:

    print("\n===== SISTEMA DE NÓMINA =====")
    print("1. Registrar empleado")
    print("2. Calcular nómina")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        salario = float(input("Salario: "))
        dias = int(input("Días trabajados: "))

        empleados.append({
            "nombre": nombre,
            "salario": salario,
            "dias": dias
        })

    elif opcion == "2":

        calcular_nomina(empleados)

    elif opcion == "3":
        break