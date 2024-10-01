# Ejercicio #1 
# Ejemplos de interfaces visuales:

# Tkinter:
# Viene preinstalado con Python, por lo que no se necesita instalar nada adicional, solo importar el modulo
# Despues se importa el modulo
import tkinter as tk

# def iniciar_tkinter():
#     # Crear la ventana principal
#     ventana = tk.Tk()
#     ventana.title("Ejemplo Tkinter")

#     # Crear un widget de etiqueta
#     etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
#     etiqueta.pack()

#     # Iniciar el bucle de eventos de Tkinter
#     ventana.mainloop()

# # Llamada de prueba para ejecutar Tkinter (se ejecutará solo cuando la función sea llamada)
# if __name__ == "__main__":
#     iniciar_tkinter()


# PyQt5:
# Se necesita ser instalado usando pip usando este comando: pip install PyQt5
# Despues se importa el modulo
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# def iniciar_pyqt5():
#     # Crear el objeto de aplicación
#     app = QApplication([])

#     # Crear la ventana principal
#     ventana = QWidget()
#     ventana.setWindowTitle('Ejemplo PyQt5')
#     ventana.setGeometry(100, 100, 280, 80)

#     # Crear un widget de etiqueta
#     etiqueta = QLabel('<h1>¡Hola, PyQt5!</h1>', parent=ventana)
#     etiqueta.move(60, 15)

#     # Mostrar la ventana
#     ventana.show()

#     # Iniciar el bucle de eventos de PyQt5
#     app.exec_()


# Flask
# Necesita ser instalado usando pip usando este comando en la interfaz: pip install Flask
# Despues se importa el modulo
from flask import Flask

def iniciar_flask():
    # Crear una instancia de la clase Flask para iniciar la aplicación
    app = Flask(__name__)

    # Definir una ruta para la URL raíz ('/') y su función asociada
    @app.route('/')
    def hola():
        # Esta función se ejecuta cuando un usuario accede a la URL raíz
        return "¡Hola, Flask en el puerto 3000!"

    # Configurar y ejecutar la aplicación Flask
    if __name__ == '__main__':
        # Ejecutar la aplicación Flask en localhost ('127.0.0.1') y en el puerto 3000
        app.run(host='127.0.0.1', port=3000, debug=True)

iniciar_flask()
