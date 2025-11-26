print("Menu\n1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius")
choice=int(input("Choose(1,2): "))
match (choice):
	case 1:
		c=float(input("Enter the temperature in Celsius: "))
		f=(c*9/5)+32
		print(f"The temperature is {f} degree Fahrenheit")
	case 2:
		f=float(input("Enter the temperature in Fahrenheit: "))
		c=(f-32)*5/9
		print(f"The temperature is {c} degree Celsius")
	case _:
		print("Invalid Choice")
		
