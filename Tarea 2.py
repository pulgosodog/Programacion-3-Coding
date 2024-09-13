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