'''If age is 5 print Go to Kindergarten
Ages 6 through 17 goes to grades 1 through 12
If age is greater than 17 say go to college
Try to complete with 10 or less lines'''

#receive age from user and store it
age = eval(input("Please type in your age: "))

#Age conditions for class assignments
if age == 5:
    print("Please go to Kindergarten")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade)) 

elif (age > 17):
    print("You are to old, please go to college")

else:
    print("You don't belong here")
