n=int(input("Enter your number: "))
if (n>1):
	for i in range(2, n//2+1):
		if (n%i==0):
			print(f"Nah, {n} is just a normal brotato")
			break
	else:
		print(f"Aye, {n} is a prime brotato")
else:
	print(f"Welp, {n} is a weird brotato, ain't prime though")

