def check_float(value):
    if isinstance(value, float):
        return value
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Valor {value} no se puede convertir a float.")

class Empleado:
  def __init__(self, n_empleado, ventas, sueldo):
    self.name = self
    self.n_empleado = n_empleado
    self.sueldo = sueldo
    self.ventas = ventas
  def mostrar_empleado(self):
        return f" n_empleado: {self.n_empleado}, ventas:{self.ventas}, sueldo:{self.sueldo}"