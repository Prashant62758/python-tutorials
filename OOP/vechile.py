class Vechile:
	def __init__(self,name,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

class Bike(Vechile):
	pass

bike_ktm = Bike('ktm duke', 240,18)
print("vechile name : ",bike_ktm.name,"\nspeed : ", bike_ktm.max_speed, "\nmileage : ", bike_ktm.mileage)
