#store the user input of 2 numbers and an operator
num1, operator, num2 = input("Enter calculation: ").split()
#convert the string to integers
num1 = int(num1)
num2 = int(num2)
#if + then we need to provide output based on addition
#print results
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))

else:
    print("Use either + - * / next time")
            
