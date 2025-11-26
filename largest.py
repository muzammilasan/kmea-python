a=int(input("Enter the First number: "))
b=int(input("Enter the Second number: "))
c=int(input("Enter the Third number: "))
if (a>b) and (a>c):
	print(f"{a} is the largest number")
elif (b>c):
	print(f"{b} is the largest number")
else:
	print(f"{c} is the largest number")

