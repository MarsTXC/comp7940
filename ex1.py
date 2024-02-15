x = 52633

print(f"factors of {x}", end=" : ")
for i in range(1,x+1):
	if x % i == 0:
		print(i, end=" ")

