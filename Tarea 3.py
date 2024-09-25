from funciones_auxiliares import check_float
from funciones_auxiliares import Empleado

# EJERCICIO 1
# Crear una aplicación que dado un monto para presupuesto anual de una
# fábrica calcule el porcentaje de dinero que le corresponde a cada
# departamento.
# Recursos Humanos 50%
# Manufactura 25%
# Empaquetado 15%
# Publicidad 10%
def presupuesto_anual(monto):
    monto = check_float(monto)
    hr =  monto * 0.50
    manufactura = monto * 0.25
    empaquetado = monto * 0.15
    publicidad = monto * 0.10
    return f"""Monto: {monto}
Recursos Humanos 50%: {hr}
Manufactura 25%: {manufactura}
Empaquetado 15%: {empaquetado}
Publicidad 10%: {publicidad}"""

# Una compañía de seguros tiene contratados a n vendedores. Cada uno
# hace tres ventas a la semana. Su política de pagos es que un vendedor
# recibe un sueldo base, y un 10% extra por comisiones de sus ventas. El
# gerente de su compañía desea saber cuánto dinero obtendrá en la semana
# cada vendedor por concepto de comisiones por las tres ventas realizadas, y
# cuanto tomando en cuenta su sueldo base y sus comisiones. Utilice una
# función para calcular la comisión por las tres ventas realizadas.

def comp_seguros(n_empleados):
    n_empleados = int(n_empleados)
    sueldo = int(input("Ingresa el sueldo base: "))
    empleados = []
    for i in range(n_empleados):
        print('Empleado', i+1)
        ventas = []
        for j in range(3):
            venta = float(input(f'Ingrese la venta {j+1}: '))
            ventas.append(venta)
        empleado = Empleado(i+1, ventas)
        empleados.append(empleado)

    for empleado in empleados:
        return f'''
Empleado {empleado.n_empleado}:
Sueldo base: {sueldo}
Venta 1: {empleado.ventas[0]} Comision 1: {empleado.ventas[0] * 0.10}
Venta 2: {empleado.ventas[1]} Comision 2: {empleado.ventas[1] * 0.10}
Venta 3: {empleado.ventas[2]} Comision 3: {empleado.ventas[2] * 0.10}
Sueldo semanal base: {sueldo / 4} Total comisiones: {(empleado.ventas[0] * 0.10) + (empleado.ventas[1] * 0.10) + (empleado.ventas[2] * 0.10)}
Sueldo semanal total: {(sueldo / 4) + (empleado.ventas[0] * 0.10) + (empleado.ventas[1] * 0.10) + (empleado.ventas[2] * 0.10)} '''


print(comp_seguros(input('Numero de empleados: ')))
