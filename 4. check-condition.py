# Define variables
x = int(input("enter the value of x:--"))
y = int(input("enter the value of y:--"))
z = int(input("enter the value of z:--"))

# Logical AND operator 
if x < y and y < z:
    print("Both conditions are true")

# Logical OR operator
if x > y or y < z:
    print("At least one condition is true")

# Logical NOT operator
if not(x == y):
    print("x is not equal to y")
