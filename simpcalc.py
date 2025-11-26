print("Simple Calculator")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("Menu\n1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)")
op=input("Choose an operator(+-*/): ")
match (op):
	case '+':
		result=num1+num2
	case '-':
		result=num1-num2
	case '*':
		result=num1*num2
	case '/':
		if (num2!=0):
			result=num1/num2
		else:
			result="Error: Division by Zero"
	case _:
		result="Error: Invalid Operator"
print(f"Result: {result}")

