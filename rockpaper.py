import random
a=['r','p,','s']
swati=0
computer=0
while True:
	d=input("enter your choice r/p/s")
	e=random.choice(a)
	if(e==d):
		print("its a tie")
	elif(d=='p'):
		if(e=='r'):
			print("Swati wins")
			swati+=1
		else:
			print("computer wins")
			computer+=1
	elif(d=='r'):
		if(e=='s'):
			print("swati wins")
			swati+=1
		else:
			print("computer wins")
			computer+=1
	elif(d=='s'):
		if(e=='p'):
			print("swati wins")
			swati+=1
		else:
			print("computer wins")
			computer+=1
	if(swati==3):
		print("swati is the winner",swati,computer)
	elif(computer==3):
		print("computer is the winner",computer,swati)
		break
