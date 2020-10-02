from math import pi
r = input("Radius of the orbit(million km):")
r = float(r)
s = input("orbit speed (km/s): ")
s = float(s)
r = r * 1000000
year = 2 * pi * r / s
year = year/(60 * 60 * 24)
print(round(year))
