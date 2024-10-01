# Ejercicio #1 
# Cómo se puede crear una aplicación de interfaz gráfica en Python, menciona los pasos y presenta un ejemplo.

# Tkinter:
# El mas popular por su simplicidad y disponibilidad.
# Viene preinstalado con Python, no se necesita instalar nada adicional, solo importar su modulo
import tkinter as tk

def iniciar_tkinter():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ejemplo Tkinter")

    # Crear un widget de etiqueta
    etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
    etiqueta.pack()

    # Iniciar el bucle de eventos de Tkinter
    ventana.mainloop()

# # PyQt5:
# Aclamado por sus funciones avanzadas y aplicaciones profesionales.
# Se necesita ser instalado usando pip usando este comando: pip install PyQt5
# Despues se importa el modulo
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

def iniciar_pyqt5():
    # Crear el objeto de aplicación
    app = QApplication([])

    # Crear la ventana principal
    ventana = QWidget()
    ventana.setWindowTitle('Ejemplo PyQt5')
    ventana.setGeometry(100, 100, 280, 80)

    # Crear un widget de etiqueta
    etiqueta = QLabel('<h1>¡Hola, PyQt5!</h1>', parent=ventana)
    etiqueta.move(60, 15)

    # Mostrar la ventana
    ventana.show()

    # Iniciar el bucle de eventos de PyQt5
    app.exec_()

# Kivy:
# Kivy es la mejor opción debido a su compatibilidad con múltiples plataformas, incluidas Android e iOS.
# Necesita ser instalado en pip usando este comando en la terminal: pip install kivy
 
# Importar las clases necesarias de Kivy
from kivy.app import App
from kivy.uix.label import Label

def iniciar_kivy():
    # Definir la aplicación Kivy como una clase que hereda de App
    class MyApp(App):
        def build(self):
            # Crear y devolver un widget de etiqueta con el mensaje
            return Label(text="¡Hola, Kivy!", font_size='40sp')

    # Ejecutar la aplicación Kivy
    MyApp().run()

# Flask:
# Dominan el desarrollo web en Python, y Dash está ganando una popularidad significativa en la comunidad de ciencia de datos.
# Necesita ser instalado usando pip usando este comando en la interfaz: pip install Flask
# Despues se importa el modulo
from flask import Flask

def iniciar_flask():
    print('!!! Visualizar en un navegador en http://localhost:3000/ !!!')
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

match(input('''Escribe el numero aosicado a la funcion que quieres correr:
1.iniciar_tkinter
2.iniciar_pyqt5
3.iniciar_flask
4.iniciar_kivy
''')):
    case("1"):
        iniciar_tkinter()
    case('2'):
        iniciar_pyqt5()
    case('3'):
        iniciar_flask()
    case('4'):
        iniciar_kivy()
    case _:
        print("Ingresa un valor correcto")