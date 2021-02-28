# Taking miles input from the user 
miles = float(input("Enter value in miles : ")) 
# conversion factor
conv_fac = 0.621371 
# calculate kilometers 
kilometers = miles /conv_fac 
print('%0.2f miles  is equal to %0.2f kilometers ' %(miles , kilometers ))

# we are getting error sine space is given @ conv_fac
#remove space , save and run

# Thank you