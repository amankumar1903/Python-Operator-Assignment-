# Define the two numbers
number1 = int(input("Enter the 1st number:--"))
number2 = int(input("Enter the 2nd number:--"))


sum_result = number1 + number2


difference_result = number1 - number2


product_result = number1 * number2


if number2 != 0:
    quotient_result = number1 / number2
else:
    quotient_result = "Division by zero is undefined"


print("Sum of two number:-", sum_result)
print("Difference of two number:-", difference_result)
print("Product of two number:-", product_result)
print("Quotient of two number:-", quotient_result)
