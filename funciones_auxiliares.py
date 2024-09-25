def check_float(value):
    if isinstance(value, float):
        return value
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Valor {value} no se puede convertir a float.")

class Empleado:
  def __init__(self, n_empleado, ventas):
    self.name = n_empleado
    self.n_empleado = n_empleado
    self.ventas = ventas
  def mostrar_ventas(self):
        return f"Empleado {self.n_empleado}, Ventas: {self.ventas}"