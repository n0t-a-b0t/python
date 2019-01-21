# Program to check if the entered number is Odd or Even
# We will first ask the user to enter a number using the raw_input() method

num = int(raw_input("Enter a number: "))

# Here, we specify 'int' in front of raw_input() for Input Formatting
# Basically, we will treat the entered numerical value as an integer

# Now, a trait of all even numbers is that they are divisible by 2
# That is, they have a remainder of zero when divided by 2
# Thus, we can use the 'Modulus' operator to get the remainder of a division operation

if num % 2 == 0:
    print "The entered number is Even"
else:
    print "The entered number is Odd"
