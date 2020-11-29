num = input("Enter a number: ")
sum1 = 0

for i in range(len(str(num))):
	sum1 += int(str(num)[i])

print(f"Sum of the digits of {num} is {sum1}")