from funciones_auxiliares import check_float, Empleado

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

# EJERCICIO 2
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
        empleado = Empleado(i+1, ventas, sueldo)
        empleados.append(empleado)
    output = ''
    for empleado in empleados:
        output = output + f'''

Empleado {empleado.n_empleado}:
Sueldo base: {sueldo}
Venta 1: {empleado.ventas[0]} Comision 1: {round(empleado.ventas[0] * 0.10, 2)}
Venta 2: {empleado.ventas[1]} Comision 2: {round(empleado.ventas[1] * 0.10, 2)}
Venta 3: {empleado.ventas[2]} Comision 3: {round(empleado.ventas[2] * 0.10, 2)}
Sueldo semanal base: {round(sueldo / 4, 2)} Total comisiones: {round((empleado.ventas[0] * 0.10) + (empleado.ventas[1] * 0.10) + (empleado.ventas[2] * 0.10), 2)}
Sueldo semanal total: {round((sueldo / 4) + (empleado.ventas[0] * 0.10) + (empleado.ventas[1] * 0.10) + (empleado.ventas[2] * 0.10), 2)} '''
    return output

# EJERCICIO 3
# Escribir un programa que permita ingresar los salarios de una cantidad
# indicada de empleados, debe presentar al final el total que se debe pagar a
# cada empleado y el descuento de renta considerando que es del 10% sobre
# cada salario.

def descuento_renta(n_empleados):
    n_empleados = int(n_empleados)
    empleados = []
    output = ''
    for i in range(n_empleados):
        sueldo = float(input(f'Ingresa el salario del empleado {i+1}: '))
        empleado = Empleado(i+1,None,sueldo)
        empleados.append(empleado)
    for empleado in empleados:
        output = output + f''' 
Empleado #{empleado.n_empleado}
Salario: {empleado.sueldo}
Salario despues de descuento de renta del 10%: {empleado.sueldo * 0.90}'''
    return output

# EJERCICIO 4
# Crear un programa que dado un monto para presupuesto anual de una
# fábrica calcule el porcentaje de dinero que le corresponde a cada
# departamento.
# Recursos Humanos 50%
# Manufactura 25%
# Empaquetado 15%
# Publicidad 10

# Reusar presupuesto_anual() pero con el presupuesto de la fabrica

# EJERCICIO 5
# Escriba un programa para capturar por teclado el número de horas
# trabajadas y que envíe dicho valor a una función que determine y retorne el
# valor a pagar, considerando que las primeras 160 horas trabajadas serán a
# $6.5 y el resto de horas a $7.5.

def n_horas_trabajadas(n_horas):
    n_horas = check_float(n_horas)
    output = None
    if n_horas >= 160:
        output = 160 * 6.5
        output = output + ((n_horas - 160) * 7.5)
    else:
        output = n_horas * 6.5
    return output

# EJERCICIO 6
# Escriba el programa que contenga una función la cual retorne el factorial de
# un número capturado por teclado.
def n_factorial(n):
    n = int(n)
    output = 1
    for i in range(n-1):
        print('')
        print('Vez',i+1)
        if(output != 1):
            print('If')
            print(f'{output} x {(i+2)}')
            output = output * (i+2)
        else:
            print('Else')
            print(f'{(i+1)} x {(i+2)}')
            output = (i+1) * (i+2)
        print('Output',output)
    return output        

# EJERCICIO 7
# Escribir el programa que tenga una función, esta devuelva el área de un
# círculo cuyo radio se le suministra como argumento.    

print(n_factorial(input('n veces: ')))
