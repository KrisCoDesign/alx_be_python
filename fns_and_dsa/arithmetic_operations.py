# num1 = float(input("Enter 1st num?: "))
# num2 = float(input("Enter 2st num?: "))
# operation = input("Operation to perform (+, -, *, /)? ")

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation =="subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "can not divide 0"
        else: 
            return num1 / num2

# result = perform_operation(num1, num2, operation)
# print(result)

