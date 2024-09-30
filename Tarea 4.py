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
        self.fecha_vencimiento = fecha_vencimiento  # Opcional, útil para productos perecederos

    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        return f"Producto: {self.nombre}\nDescripción: {self.descripcion}\nCategoría: {self.categoria}\nPrecio: ${self.precio}\nCantidad Disponible: {self.cantidad_disponible}\nCódigo del Producto: {self.codigo_producto}\nProveedor: {self.proveedor}\nFecha de Vencimiento: {self.fecha_vencimiento or 'N/A'}"

    # Método para actualizar el stock
    def actualizar_stock(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    # Método para actualizar el precio
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para aplicar descuento
    def aplicar_descuento(self, porcentaje_descuento):
        self.precio -= self.precio * (porcentaje_descuento / 100)

# Contador de producción
class GestorPresupuesto:
    def __init__(self, presupuesto_asignado):
        self.presupuesto_asignado = presupuesto_asignado  # Presupuesto asignado
        self.costos = []  # Lista para almacenar los costos
        self.total_costos = 0  # Total de costos
        self.facturas = []  # Lista para almacenar facturas
        self.caja_chica = 0  # Monto de caja chica

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
