number = str(input("Enter a number: "))
string = str(number)
new_string = ""

for i in range(len(string)):
	new_string += string[-i-1]

if string == new_string:
	print(f"{number} is a palindrome")
else:
	print(f"{number} is not a palindrome")