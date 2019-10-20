class Cajero:
	def __init__(self, dinero = 250000, calle = ""):
		self.calle = calle
		self.dinero = dinero

	def extraer(self, cantidad):
		if cantidad <= self.dinero:
			self.dinero -= cantidad
			print("Extraccion exitosa, su saldo actual es de $"+str(self.dinero)+ ".")
		else:
			print("No hay dinero suficiente")

	def depositar(self, cantidad):
		self.dinero += cantidad
		print("Ha depositado la cantida de $"+str(cantidad)+", su saldo actual es de\
 $"+str(self.dinero)+".")


#class Usuario:
#	def __init__(self, )

cajero13 = Cajero(100000)
cajero13.calle = "13 y 47"
print(cajero13.calle, cajero13.dinero)
cajero13.extraer(834)
cajero13.depositar(300000)

