# class Coche:
#   def __initialize_(self, marca, model):
#     self.marca = make
#     self.modelo = modelo
#     self.velocidad = 0
    
#   def acelerar(self, valor):
#     self.velocidad += valor
#     print(f"La velocidad aumentó y tiene un valor de {self.velocidad}")
        
#   def desacelerar(self, valor):
#     self. -= valor
#     print("La velocidad disminuyó y tiene un valor de {self.velocidad}")

# Ejemplo esperado
# mi_coche = Coche("Toyota", "Corolla")
# mi_coche.acelerar(20)
# mi_coche.desacelerar[5]


class Coche:
  def __init__(self, marca, modelo):  
    self.marca = marca  
    self.modelo = modelo  
    self.velocidad = 0  
    
  def acelerar(self, valor):
    self.velocidad += valor  
    print(f"La velocidad aumentó y tiene un valor de {self.velocidad}")
        
  def desacelerar(self, valor):
    self.velocidad -= valor 
    print(f"La velocidad disminuyó y tiene un valor de {self.velocidad}")
