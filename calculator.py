def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt the user to choose an operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_sign = '/'
        else:
            result = "undefined (cannot divide by zero)"
            operation_sign = '/'
    else:
        result = "invalid operation"
        operation_sign = ''
    
    # Display the result
    if operation_sign:
        print(f"The result of {num1} {operation_sign} {num2} is: {result}")
    else:
        print(result)

# Run the calculator
calculator()
