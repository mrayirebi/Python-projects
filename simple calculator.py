while True:
    print("options:")
    print("enter 'add' to add two numbers")
    print("enter 'subtract' to subtract two numbers")
    print("enter 'multiply' to multiply two numbers")
    print("enter 'divide' to divide two numbers")
    user_input=input(":")

    if user_input == "quit":
        print("Goodbye, see you next time")
        break
    
    elif user_input=="add":
        num1 = float(input("Enter a number of choice:"))
        num2 = float(input("Enter your second number genius:"))
        result = str(num1 + num2)
        print("The answer is " + result)

    elif user_input=="subtract":
        num1 = float(input("Enter a number of choice:"))
        num2 = float(input("Enter your second number genius:"))
        result = str(num1 - num2)
        print("The answer is " + result)

    elif user_input=="multiply":
        num1 = float(input("Enter a number of choice:"))
        num2 = float(input("Enter your second number genius:"))
        result = str(num1 * num2)
        print("The answer is " + result)

    elif user_input=="divide":
        num1 = float(input("Enter a number of choice:"))
        num2 = float(input("Enter your second number genius:"))
        result = str(num1 / num2)
        print("The answer is " + result)

    else:
        print("Unknown input, you had one job!!!!!!")
