print("""Escribe el numero asociado a la herramienta que quiere correr
1. Promedio de tres numeros
2. Precio de producto mas IVA
3. Aumentar el salario 25%
4. Intercambiar valor de dos numeros
5. Potenciar un numero
6. Calculadora de edad
7. Cacula el total por compra de articulos (con inpuestos)""")
respuesta = input()

match respuesta:
        case "1":
            print("Ingresa 3 numeros para recibir su promedio")
            numeros = []
            for i in range(3):
                numeros.append(int(input(f"Numero {i + 1}: ")))
            print((numeros[0] + números[1] + números[2]) / 3)
        case "2":
             inpuesto = int(input(f"Ingrese el precio del producto para calcular el impuesto: "))
             inpuesto = inpuesto * 1.15
             print(f"El precio del producto mas el inpuesto es {inpuesto}")
        case "3":
            salario = int(input(f"Ingrese el salario a aunmentar el 25%:  "))
            salario = salario * 1.25
            print(f"El salario incrementado al 25% es {salario}")
        case "4":
            print(f"Ingrese dos numeros para intercambiar sus valores")
            a = int(input(f"Numero a: "))
            b = int(input(f"Numero b: "))
            holder = a
            a = b
            b = holder
            print("")
            print(f"Numero a es igual a {a}")
            print(f"Numero b es igual a {b}")
        case "5":
             base = int(input(f"Ingresa el numero base a potenciar: "))
             potencia = int(input(f"Ingrese el numero potencia: "))
             print(f"{base} potenciado a {potencia} es igual a {base ** potencia}")
        case "6":
            year = 2024
            nacimiento = int(input(f"Ingresa la fecha de nacimiento: "))
            print(f"Tiene {year-nacimiento} años de edad")

        case "7":
            articulos = []
            articulos.append(int(input(f"Precio del primer articulo: ")))
            otro = int(input(f"Desea agregar otro articulo? 0 = No | 1 = Si: "))
            while otro:
                articulos.append(int(input(f"Precio del articulo: ")))
                otro = int(input(f"Desea agregar otro articulo? 0 = No | 1 = Si: "))
                suma = 0
            for i in articulos:
                suma += i
            print(f"Precio total de articulos con inpuestos del 10%: {suma}")
        case _:
            print('Escribe un numero para correr el ejercicio asociado a el')
