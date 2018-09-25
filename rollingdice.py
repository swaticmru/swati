#rolling a dice
import random
while True:
	a=input("choose an action")
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		print("quit")
		break