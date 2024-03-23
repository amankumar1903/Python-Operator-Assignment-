# Define a number
num = int(input("enter num to check:--"))

# Using the ternary operator to assign a value based on the condition
res = "Positive" if num > 0 else ("Zero" if num == 0 else "Negative")

# Print the value of res
print("The number is: ", res)
