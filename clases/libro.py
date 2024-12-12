class Libro:
  def __init__(self, titulo, autor, numero_paginas):
    self.titulo = titulo
    self.autor = autor
    self.numero_paginas = numero_paginas

  def descripcion(self):
    return f"{self.titulo} es un libro escrito por {self.autor} y tiene {self.numero_paginas} páginas."