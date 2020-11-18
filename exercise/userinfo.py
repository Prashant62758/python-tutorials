user = {}
name = input('enter your name : ')
age = int(input('enter your age : '))
movies = input('enter you favorite movies seperated by comma(,) :  ').split(',')
songs = input('enter your favorite songs seperated by comma(,) : ').split(',')

user['name'] = name
user['age'] = age
user['movies'] = movies
user['songs'] = songs

for key , value in user.items():
	print(f"{key} : {value}")
