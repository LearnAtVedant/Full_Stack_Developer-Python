# We will take input from end users .
#Variable Kilometer

Kilometers = float(input(' Enter value in kilometers : '))

#float is data type
#input in inbuilt method to take user input

# Conversion factor
Conv_fact=0.621371

# its a const value

# now will find miles

miles = Kilometers * Conv_fact

# now we will print the out put

print(' %0.2f kilometers is equal to %0.2f miles' %(Kilometers,miles))

#save and run