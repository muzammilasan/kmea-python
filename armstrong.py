num = int(input("Enter the number: "))
sum = 0
temp = num
while(temp > 0):
	digit = temp%10
	sum = sum + digit**3
	temp = temp//10
if sum == num:
	print("It's an armstrong number")
else:
	print("It's not an armstrong number")
