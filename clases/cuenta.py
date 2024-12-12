class CuentaBancaria:
  def __init__(self):
    self.__saldo = 0

  def depositar(self, monto):
    self.__saldo += monto

  def retirar(self, monto):
    if monto <= self.__saldo:
      self.__saldo -= monto

  def consultar_saldo(self):
    return self.__saldo
