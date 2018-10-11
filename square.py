#to find the square of any number
a=float(input("enter a number of your choice:"))
b=float(input("enter the second choice:"))
c=input("choose the operation +,-,/,*,**")
if(c=="+"):
	print(a+b)
elif(c=="-"):
	print(a-b)
elif(c=="*"):
	print(a*b)
elif(c=="/"):
	print(a/b)
elif(c=="**"):
	print(a**b)
else:
	print("invalid input")