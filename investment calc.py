#have the user enter their investement amount and expected interest
#Each year their investment will increase by their investment + their investment * interest
#Print out the earnings after a 10 year period

#Take input from user and convert it to a float
ivsmnt, intrst = input("Please enter your current investment and expected interest: ").split()
ivsmnt = float(ivsmnt)

#convert interest rate to percentage
intrst = float(intrst) * .01

#Calculate for returns every year
#rtn_per_yr = ivsmnt + ivsmnt * intrst
#rtn_per_decade = rtn_per_yr * 10
for i in range (10):
    ivsmnt = ivsmnt + ivsmnt * intrst

print("After a 10 year period, your earnings should be {:.2f}".format(ivsmnt))






