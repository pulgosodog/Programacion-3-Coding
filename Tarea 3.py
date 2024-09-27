from funciones_auxiliares import check_float, Empleado
import math
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
        if(output != 1):
            output = output * (i+2)
        else:
            output = (i+1) * (i+2)
    return output        

# EJERCICIO 7
# Escribir el programa que tenga una función, esta devuelva el área de un
# círculo cuyo radio se le suministra como argumento.    
def area_circulo(radio):
    radio = check_float(radio)
    return round(math.pi*(radio**2),2)

# EJERCICIO 8
# Programa para pasar tres argumentos reales a una función que devolverá
# el menor de ellos.

def menor_de_tres(n1,n2,n3):
    arr = [n1, n2, n3]
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    arr.sort()
    return arr

#Ingresar datos de la siguiente manera -> print(menor_de_tres(input('n1 '),input('n2 '),input('n3 ')))

# EJERCICIO 9
# Crear una función que reciba como argumento el importe de una compra y
# devuelva la cantidad final a pagar, teniendo en cuenta que los descuentos
# son del 5% cuando se compra más de 300 €, del 10% cuando se compra
# más de 500 € y del 12% para cantidades mayores de 500(Lo voy a cambiar a 600 porque es lo mismo que el anterior) €, escribe un
# programa que pregunte al usuario la cantidad comprada y le indique el
# importe a pagar.

def final_pagar(importe):
    importe = check_float(importe)
    if importe > 600:
        return f"""Descuento del 12% a {importe}
Debe pagar {importe * 0.90}"""
    elif importe > 500:
        return f"""Descuento del 10% a {importe}
Debe pagar {importe * 0.90}"""
    elif importe > 300:
        return f""""Descuento del 5% a {importe}
Debe pagar {importe * 0.95}"""
    else:
        return f'''Sin descuento aplicable
Debe pagar {importe}'''
    
# EJERCICIO 10
# Haz un programa que pregunte al usuario un número entero y que
# mediante una función imprima la tabla de multiplicar (del 1 al 10) de dicho
# número.

def tabla_multiplicar(n):
    n = int(n)
    output = ''''''
    for i in range(10):
        output = output + f'''
{n} x {i+1} = {n*(i+1)}'''
    return output

def menu():
    while True:
        print("""
        Escribe el número asociado a la herramienta que quieres correr:
        1. Presupuesto anual por departamento
        2. Calcular comisiones de empleados de seguros
        3. Calcular salario con descuento de renta
        4. Reusar presupuesto anual para fábrica
        5. Calcular pago por horas trabajadas
        6. Calcular factorial de un número
        7. Calcular área de un círculo
        8. Encontrar el menor de tres números
        9. Calcular descuento basado en importe de compra
        10. Imprimir tabla de multiplicar
        11. Salir
        """)
        
        respuesta = input("Selecciona una opción: ")

        match respuesta:
            case "1":
                monto = input("Introduce el monto del presupuesto anual: ")
                print(presupuesto_anual(monto))
            case "2":
                n_empleados = input("Introduce el número de empleados: ")
                print(comp_seguros(n_empleados))
            case "3":
                n_empleados = input("Introduce el número de empleados: ")
                print(descuento_renta(n_empleados))
            case "4":
                monto = input("Introduce el monto del presupuesto anual de la fábrica: ")
                print(presupuesto_anual(monto))
            case "5":
                n_horas = input("Introduce el número de horas trabajadas: ")
                print(n_horas_trabajadas(n_horas))
            case "6":
                n = input("Introduce un número para calcular el factorial: ")
                print(n_factorial(n))
            case "7":
                radio = input("Introduce el radio del círculo: ")
                print(area_circulo(radio))
            case "8":
                n1 = input("Introduce el primer número: ")
                n2 = input("Introduce el segundo número: ")
                n3 = input("Introduce el tercer número: ")
                print(menor_de_tres(n1, n2, n3))
            case "9":
                importe = input("Introduce el importe de la compra: ")
                print(final_pagar(importe))
            case "10":
                n = input("Introduce un número para la tabla de multiplicar: ")
                print(tabla_multiplicar(n))
            case "11":
                print("Saliendo del programa...")
                break
            case _:
                print("Escribe un número válido para correr el ejercicio asociado.")
    
menu()
