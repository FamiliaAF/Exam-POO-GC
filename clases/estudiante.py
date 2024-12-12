class Estudiante:
  numero_estudiantes = 0

  def __init__(self, nombre, grado):
    self.nombre = nombre
    self.grado = grado
    Estudiante.numero_estudiantes += 1