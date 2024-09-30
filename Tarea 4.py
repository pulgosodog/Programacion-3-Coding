import math

# Ejercicios de la presentacion
# Realice las siguientes abstracciones:
# Datos generales de un empleado.
class Empleado:
    def __init__(self, id, nombre1, nombre2, apellido1, apellido2, direccion,  num_telefono, salario_mensual, puesto):
        self.id = id
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.direccion = direccion
        self.num_telefono = num_telefono
        self.salario_mensual = salario_mensual
        self.puesto = puesto

    def nombre_completo(self):
        return f'{self.nombre1} {self.nombre2} {self.apellido1} {self.apellido2}'
    
    def mostrar_direccion(self):
        return self.direccion
    
    def telefono_formateado(self):
        return self.num_telefono
    
    def mostrar_puesto(self):
        return self.puesto
    
    def salario_anual(self):
        return self.salario_mensual * 12
    
    def salario_anual(self):
        return self.salario_mensual * 12
    
    def actualizar_datos(self, nueva_direccion=None, nuevo_telefono=None, nuevo_puesto=None, nuevo_salario=None):
        if nueva_direccion:
            self.direccion = nueva_direccion
        if nuevo_telefono:
            self.num_telefono = nuevo_telefono
        if nuevo_puesto:
            self.puesto = nuevo_puesto
        if nuevo_salario:
            self.salario_mensual = nuevo_salario
    
    def  __str__(self):
        return f'ID: {self.id}\nNombre: {self.nombre_completo()}\nDirección: {self.direccion}\nTeléfono: {self.num_telefono}\nSalario Mensual: {self.salario_mensual}\nPuesto: {self.puesto}'

# Datos generales de un estudiante.
class Estudiante:
    def __init__(self, nombre_completo, fecha_nacimiento, sexo, direccion, padres, contacto_padres, grado_escolar, historial_calificaciones, tutor_asignado):
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.direccion = direccion
        self.padres = padres  # {'nombre_padre': '', 'nombre_madre': ''} o {'tutor': ''}
        self.contacto_padres = contacto_padres  # {'telefono_padre': '', 'telefono_madre': ''} o {'telefono_tutor': ''}
        self.grado_escolar = grado_escolar  # Ejemplo: "5to Grado" (string que representa el nivel educativo)
        self.historial_calificaciones = historial_calificaciones  # Formato: {'semestre1': {'parcial1': nota, 'parcial2': nota}, ... }
        self.tutor_asignado = tutor_asignado

    def __str__(self):
        return (f"Nombre completo: {self.nombre_completo}\n"
                f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
                f"Sexo: {self.sexo}\n"
                f"Dirección: {self.direccion}\n"
                f"Grado escolar: {self.grado_escolar}\n"
                f"Tutor asignado: {self.tutor_asignado}\n"
                f"Contactos de los padres: {self.contacto_padres}\n"
                f"Historial de calificaciones: {self.historial_calificaciones}")

    def actualizar_datos(self, nueva_direccion=None, nuevo_contacto_padres=None, nuevo_grado_escolar=None, nuevo_tutor_asignado=None):
        if nueva_direccion:
            self.direccion = nueva_direccion
        if nuevo_contacto_padres:
            self.contacto_padres = nuevo_contacto_padres
        if nuevo_grado_escolar:
            self.grado_escolar = nuevo_grado_escolar
        if nuevo_tutor_asignado:
            self.tutor_asignado = nuevo_tutor_asignado

    def agregar_calificacion(self, semestre, parcial, nota):
        if semestre not in self.historial_calificaciones:
            self.historial_calificaciones[semestre] = {}
        self.historial_calificaciones[semestre][parcial] = nota

    def promedio_por_semestre(self, semestre):
        if semestre in self.historial_calificaciones:
            notas = self.historial_calificaciones[semestre].values()
            return sum(notas) / len(notas)
        return None

# Datos generales de un producto.
class Producto:
    def __init__(self, nombre, descripcion, categoria, precio, cantidad_disponible, codigo_producto, proveedor, fecha_vencimiento=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo_producto = codigo_producto
        self.proveedor = proveedor
        self.fecha_vencimiento = fecha_vencimiento 

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}\nDescripción: {self.descripcion}\nCategoría: {self.categoria}\nPrecio: ${self.precio}\nCantidad Disponible: {self.cantidad_disponible}\nCódigo del Producto: {self.codigo_producto}\nProveedor: {self.proveedor}\nFecha de Vencimiento: {self.fecha_vencimiento or 'N/A'}"

    def actualizar_stock(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def aplicar_descuento(self, porcentaje_descuento):
        self.precio -= self.precio * (porcentaje_descuento / 100)

# Contador de producción
class GestorPresupuesto:
    def __init__(self, presupuesto_asignado):
        self.presupuesto_asignado = presupuesto_asignado 
        self.costos = []  
        self.total_costos = 0  
        self.facturas = []  
        self.caja_chica = 0  

    def registrar_costo(self, descripcion, monto):
        self.costos.append({'descripcion': descripcion, 'monto': monto})
        self.total_costos += monto
        print(f"Costo registrado: {descripcion} - Monto: {monto}")

    def procesar_factura(self, proveedor, monto):
        self.facturas.append({'proveedor': proveedor, 'monto': monto})
        self.total_costos += monto
        print(f"Factura procesada: {proveedor} - Monto: {monto}")

    def manejar_caja_chica(self, monto):
        self.caja_chica += monto
        print(f"Caja chica ajustada: Monto actual: {self.caja_chica}")

    def comparar_costos_con_presupuesto(self):
        diferencia = self.presupuesto_asignado - self.total_costos
        if diferencia >= 0:
            print(f"Gastos dentro del presupuesto. Restante: {diferencia}")
        else:
            print(f"Gastos exceden el presupuesto por: {-diferencia}")

    def __str__(self):
        print(f"Presupuesto asignado: {self.presupuesto_asignado}")
        print(f"Total de costos: {self.total_costos}")
        print(f"Total en caja chica: {self.caja_chica}")


# EJERCICIOS PROPUESTOS DE CLASES, ATRIBUTOS Y MÉTODOS

# 1. Desarrollar un programa que tenga una clase que represente un Cuadrado y
# tenga los siguientes métodos: ingresar valor a su lado, imprimir su perímetro y su
# superficie.

class Cuadrado:
    def __init__(self, lado = 0):
        self.lado = lado

    def ingresar_lado(self, nuevo_lado):
        self.lado = nuevo_lado
        print(f"Lado del cuadrado actualizado a: {self.lado}")

    def calcular_perimetro(self):
        return 4 * self.lado

    def calcular_superficie(self):
        return self.lado ** 2

    def imprimir_perimetro(self):
        perimetro = self.calcular_perimetro()
        print(f"El perímetro del cuadrado es: {perimetro}")

    def imprimir_superficie(self):
        superficie = self.calcular_superficie()
        print(f"La superficie del cuadrado es: {superficie}")

# 2. Implementar la clase operaciones. Se deben ingresar los dos valores enteros,
# calcular su suma, resta, multiplicación y división, cada una en un método, e
# imprimir dichos resultados.

class Operaciones:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 == 0:
            return "Error: División por cero"
        return self.valor1 / self.valor2

    def imprimir_resultados(self):
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")

# 3. Diseñe una clase y cree un objeto que tenga un atributo (con su respectiva
# propiedad) para capturar un número entero y determinar si es positivo, negativo o
# cero. Implementar un método (función) que devuelva el mensaje correspondiente.

class Numero:
    def __init__(self, numero):
        self.numero = numero

    def evaluar_numero(self):
        if self.numero > 0:
            return "El número es positivo."
        elif self.numero < 0:
            return "El número es negativo."
        else:
            return "El número es cero."

# 4. Resuelva el siguiente problema: Leer dos números del teclado y multiplicarlos si
# son iguales, restarlos si el primero es mayor que el segundo o sumarlos si el
# primero es menor que el segundo. Diseñe la clase con los atributos, métodos y
# propiedades requeridos

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2  

    def calcular(self):
        if self.numero1 == self.numero2:
            resultado = self.numero1 * self.numero2
            operacion = "multiplicación"
        elif self.numero1 > self.numero2:
            resultado = self.numero1 - self.numero2
            operacion = "resta"
        else:
            resultado = self.numero1 + self.numero2
            operacion = "suma"

        print(f'''La operacion utilizada fue {operacion}
El resultado fue: {resultado}''')
        return resultado

# 5. Diseñe una clase y cree un objeto que tenga un atributo (con su respectiva
# propiedad) para capturar el nombre de un día de la semana y determinar si es día
# de pago (el día de pago es el viernes). Implementar un método (función) que
# devuelva el valor booleano true si es día de pago o false en caso contrario.

class DiaDePago:
    def __init__(self, dia):
        self.dia = dia.lower()

    def pago(self):
        return self.dia == 'viernes'
    
# 6. Defina una clase para representar una cuenta bancaria. Los miembros de datos
# deben incluir el nombre del depositante, el número de cuenta y el saldo. Las
# funciones de los miembros deben permitir lo siguiente:
# • Crear un objeto e inicializarlo
# • Visualización del nombre, el número de cuenta y el saldo del depositante
# • Depositar una cantidad de dinero dada por un argumento
# • Retirar una cantidad de dinero dada por un argumento

class CuentaBancaria:
    def __init__(self, nombre, numero_cuenta, saldo=0):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta 
        self.saldo = saldo  

    def visualizar_informacion(self):
        print(f"Nombre: {self.nombre}, Cuenta: {self.numero_cuenta}, Saldo: {self.saldo:.2f} USD")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depositado: {cantidad:.2f} USD. Nuevo saldo: {self.saldo:.2f} USD")
        else:
            print("Cantidad debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0  and self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retirado: {cantidad:.2f} USD. Saldo restante: {self.saldo:.2f} USD")
        else:
            print("Cantidad debe ser mayor que cero y no exceder el saldo.")

# 7. Desarrollar un programa que tenga una clase que represente un Triángulo y
# tenga los siguientes métodos: ingresar valor a sus lados, imprimir su área,
# clasificar el tipo de triángulo en escaleno, isósceles o equilátero.

class Triangulo:
    def __init__(self, lado1=0, lado2=0, lado3=0):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ingresar_lados(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        semi_perimetro = (self.lado1 + self.lado2 + self.lado3) / 2
        #Fórmula de Herón
        area = math.sqrt(semi_perimetro * (semi_perimetro - self.lado1) * (semi_perimetro - self.lado2) * (semi_perimetro - self.lado3))
        return area

    def clasificar(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"