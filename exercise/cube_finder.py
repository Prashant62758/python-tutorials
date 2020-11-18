def cubes_fun(n):
	cubes = {}
	for i in range(1, n+1):
		cubes[i] = i ** 3
	return cubes
print(cubes_fun(10))
