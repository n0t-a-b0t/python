# Program for finding the greater of the two entered integers
# we will first input the integers from the user
num1 = int(raw_input("Enter first integer: "))
num2 = int(raw_input("Enter second integer: "))

# Now, we will compare the entered integers
# First, we will see if the first integer is greater than the second
if num1 > num2:
    print "%d is greater" % num1

# Now, if the first integer is not greater than the second, we will check if the second integer is greater than the
# first
# The 'else if' statement in python is written as 'elif'
elif num2 > num1:
    print "%d is greater" % num2

# Since none of the integers id greater, they have to be equal
# We will write an else condition for this scenario
else:
    print "Both the entered integers are equal"
