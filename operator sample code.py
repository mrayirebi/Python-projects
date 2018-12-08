#take two numbers from user and store them in a variable
num1, num2 = input("Please enter two numbers: ").split()

#convert the two numbers to integer values
num1 = int(num1)
num2 = int(num2)

#add the two numbers
sum = num1 + num2

#find the difference
difference = num1 - num2

#multiply the two numbers
multiply = num1 * num2

#Divide the values
quotient = num1 / num2

#find the remainder
remainder = num1 % num2

#print the results as follows "num1 + num2 = sum"
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, multiply))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
