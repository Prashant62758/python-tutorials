class Vechile:
	def __init__(self,max_speed,mileage):
		self.max_speed = max_speed
		self.mileage = mileage

modelX = Vechile(240,180)
print("speed : ", modelX.max_speed, "mileage : ", modelX.mileage)
