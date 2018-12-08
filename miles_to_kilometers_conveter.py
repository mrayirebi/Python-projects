'''Problem : Receive miles and convert to kilometers

Kilometers = miles * 1.60934

Enter miles 5

Output should look like: 5 miles equals 8.04 kilometers'''

#Ask user to input miles and store it in th miles_frm_usr variable
miles_frm_usr = int(input('Please enter miles to convert to kilometers: '))

#Perform calculation by multiplying 1.60934 by miles_frm_usr
kilometers_to_display = miles_frm_usr * 1.60934

#print results using format()
#print(miles_frm_usr," miles equals ", kilometers_to_display, " kilometers.")
print("{} miles equals {} kilometers".format(miles_frm_usr, kilometers_to_display))
