def calcular_nomina(empleados):

    for empleado in empleados:

        salario_base = empleado["salario"]
        dias = empleado["dias"]

        salario_dias = (salario_base / 30) * dias

        auxilio = 0

        if salario_base < 2600000:
            auxilio = 160000

        descuento = salario_dias * 0.08

        total = salario_dias + auxilio - descuento

        print("\n===== DESPRENDIBLE =====")
        print("Empleado:", empleado["nombre"])
        print("Total a pagar:", total)