# Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como
# el número introducido.
def ejercicio_1():
    nombre = input("Escribe tu nombre: ")
    numero = int(input("Escribe un numero "))
    for i in range(numero):
        print(nombre)

# Escribir un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con todas
# las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra
# del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre
# combinando mayúsculas y minúsculas como quiera.
def ejercicio_2():
  nombre = input("Escribe tu nombre completo: ")
  for i in range(3):
    print(nombre)
  for i in range(3):
    print(nombre.lower())
  for i in range(3):
    print(nombre.upper())
  for i in range(3):
    nombre = nombre.lower()
    array = nombre.split()
    for j in range(len(array)):
        array[j] = list(array[j])
        array[j][0] = array[j][0].upper()
        array[j] = ''.join(array[j])
    print(' '.join(array))

# Escribir un programa que pregunte el nombre del usuario en la consola y después de
# que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
# <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que
# tienen el nombre.
def ejercicio_3():
   nombre = input('Introduce un nombre: ')
   nombre = nombre.upper()
   n = len(list(nombre))
   print(nombre, n)
    
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación
# aritmética:
#(3+2/2*5)^2
# - Presentar también la solución para valores desconocidos, es decir leer los datos.
def ejercicio_4():
    print('((3+2)/(2 * 5))^2) =', ((3+2)/(2 * 5))**2)
    print('Presenta datos para la solucion: (a/b)^2)')
    a = int(input('a: '))
    b = int(input('b: '))
    resultado = ((a/b)**2)
    print('Resultado: ', resultado)

# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n
# primeros enteros positivos puede ser calculada de la siguiente forma:
#(n(n+1))/2
def ejercicio_5():
   print('Escribe el valor n: ')
   n = float(input('n: '))
   resultado = (n*(n+1))/2
   print(resultado)

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
# el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la
# frase Tu índice de masa corporal es <imc>; donde <imc> es el índice de masa corporal
# calculado redondeado con dos decimales.
def ejercicio_6():
   kg = float(input('Escribe tu peso en kg: '))
   mts = float(input('Escribe tu estatura en metros: '))
   imc = kg/mts**2
   print('Tu IMC es ', round(imc,2))

print("""Escribe el numero asociado a la herramienta que quiere correr
1. Nombre numero de veces
2. Nombre completo 3 veces, 1 mayus, 1 min, 1ra letra de apellidos y nombre en masyus
3. Nombre mayus y numero de letras de nombre
4. Operacion ((3+2)/(2 * 5))^2) e introducir nuevos datos
5. Introducir n y realizar (n*(n+1))/2
6. Calculadora IMC""")
respuesta = input()
match respuesta:
        case "1":
          ejercicio_1()
        case "2":
          ejercicio_2()
        case "3":
          ejercicio_3()
        case "4":
          ejercicio_4()
        case "5":
          ejercicio_5()
        case "6":
          ejercicio_6()
        case _:
            print('Escribe un numero para correr el ejercicio asociado a el')
