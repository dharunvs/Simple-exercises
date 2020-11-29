string = str(input("Enter a number: "))
new_string = ""

for i in range(len(string)):
	new_string += string[-i-1]

print(f"Reverse of {string} is {new_string}")