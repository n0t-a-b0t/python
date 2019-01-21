# Program to demonstrate lambda function in Python
# Lambda is an anonymous function in Python which takes in any number of arguments but only one expression
n = int(raw_input("Enter a number to increment by 50: "))
x = lambda a: a + 50
print "Output: ", (x(n))

m = int(raw_input("Enter the first multiplier: "))
o = int(raw_input("Enter the second multiplier: "))
y = lambda b, c: b * c
print "Output: ", (y(m, o))


# We can create a lambda function inside another function and then use the same function for multiple situations


def multiplier(p):
    return lambda d: d * p


timestwo = multiplier(2)
timesthree = multiplier(3)

j = int(raw_input("Enter a number: "))
i = int(raw_input("Multiply by 2 or 3?: "))
if i == 2:
    print "Times two: ", timestwo(j)
    # Here, timestwo needs two values, one for d and another for p. p is already set to 2, thus, we input only one value
elif i == 3:
    print "Times three: ", timesthree(j)
    # Here timesthree needs two values, for d and p. p is already set to 3, so we input only one value
else:
    print "Enter either 2 or 3"
