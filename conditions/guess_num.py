from random import randint

guess_num =  randint(1,20)

user_num = -1
try_count = 1

while guess_num != user_num:
	print("%d try : " % try_count, end='' )
	user_num = int(input("enter number between 1 to 20 that you guess: "))
	if user_num < guess_num:
		print("Too less.")
	elif user_num > guess_num:
		print("too high.")
	else:
		print("you guessed it.")
	try_count += 1
