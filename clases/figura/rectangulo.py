from figura.figura import Figura

class Rectangulo(Figura):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
    return f"El área del rectángulo es {self.base * self.altura}."
