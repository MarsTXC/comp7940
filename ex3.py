l = [52633, 8137, 1024, 999]

def print_factors(x):
	print(f"Factors of {x}", end=" : ")# f for f-string, it can allows to embed experssions inside string literals 
	for i in range(1, x + 1):
		if x % i == 0:
			print(i, end=" ")

def print_factors_of_list(l):
	for num in l:
		print_factors(num)
		print("\n")# Separate factors of different numbers

print_factors_of_list(l)
