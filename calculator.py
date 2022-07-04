
def get_calculation (num1,num2,operation):
	if operation == "+":
		print(f"The answer is {int(num1)+ int(num2)}")
	elif operation == "-":
		print(f"The answer is {int(num1) - int(num2)}")	
	elif operation == "/":
		print(f"The answer is {int(num1)/ int(num2)}")
	elif operation == "*":
		print(f"The answer is {int(num1)* int(num2)}")
	else:
		print("invalid operation")
		return None


def main():
	num1= input("Enter the first number:")
	num2=input("Enter the second number:")
	
	if num1.isdigit() and num2.isdigit():
		operation=input("Choose the operation (+, -, /, *):") 
		answer = get_calculation(num1,num2,operation)
	else:
		print("The input is not number ")



		
		


	



if __name__ == '__main__':
	main()
