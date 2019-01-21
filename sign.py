# Program to create own dictionary
# We will import the operator dictionary for arithmetic operations
import operator

# We will define three variables, two for the two integers and one for the sign/operator
num1 = int(raw_input())
num2 = int(raw_input())
sign = raw_input()

# We will now create our own key:value pairs for the four sign inputs
sign_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

# We will now perform the respective arithmetic operation on the integers and print out the result
print sign_dict[sign](num1, num2)
