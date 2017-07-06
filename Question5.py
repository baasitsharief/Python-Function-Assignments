import random

def roll_dice(n,m):
	if(n<4):
		print("Error: Number of sides is less than 4")
	else:
		for i in range(m):
			print(random.randint(1,n))
		print("That's all")
		return