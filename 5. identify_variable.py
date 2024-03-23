# Defining  two variables which may be similar or not, we assume not similar. 
var1 = [1, 2, 3]
var2 = [1, 2, 5]

# checking 1st time
if var1 is var2:
    print("var1 and var2 are the same object.")
else:
    print("var1 and var2 are not the same object.")

# Now let's make var2 point to the same object as var1
var2 == var1

# Check again
if var1 is var2:
    print("Now, var1 and var2 are the same object.")
else:
    print("Even now, var1 and var2 are not the same object.")
