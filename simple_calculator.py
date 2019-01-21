# Program to implement simple mathematical operations: addition, subtraction, multiplication and division
# We will input two integers from the user

num1 = int(raw_input("Enter the First Number: "))
num2 = int(raw_input("Enter the Second Number: "))
num3 = int(raw_input("Enter operation: 1: Add, 2: Subtract, 3: Multiply, 4: Divide, 5: Abs-Divide: "))

# Addition
if num3 == 1:
    addition = num1 + num2
    print "The sum of the entered numbers is: %d" % addition

# Subtraction
if num3 == 2:
    subtraction = abs(num1 - num2)
    print "The difference between the entered values is: %d" % subtraction

# Multiplication
if num3 == 3:
    multiplication = num1 * num2
    print "The product of the entered numbers is: %d" % multiplication

# Division
# Here, divmod(a, b) gives the quotient and remainder when a is divided by b
if num3 == 4:
    division = divmod(num1, num2)
    print "The quotient and remainder when num1 is divided by num2 is: %d\t%d" % division

# Absolute Division
# For accurate division results, we will convert num1 and num2 to float data type from integer data type
# Then we can divide them and get float point value as the answer, which would be accurate
# This is because simply dividing them as integer types would truncate the decimal part of the output
# Float data type is denoted by %f
if num3 == 5:
    float_num1 = float(num1)
    float_num2 = float(num2)
    absolute_division = float_num1 / float_num2
    print "The absolute division is: %f" % absolute_division

# The simple calculator program ends here
