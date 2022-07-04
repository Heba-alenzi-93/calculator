
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
		return None


def main():
	num1= input("Enter the first number:")
	num2=input("Enter the second number:")
	
	if num1.isdigit() and num2.isdigit():
		operation=input("Choose the operation (+, -, /, *):") 
		answer = get_calculation(num1,num2,operation)
		if answer == None:
			print("The operation is not valid ")
		else:
			print("the answer is "+ str(answer))
	else:
		print("The input is not number ")



		
		


	



if __name__ == '__main__':
	main()
