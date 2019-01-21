# Program to find prime numbers between two intervals
# We will take in the lower and upper limits
a = int(raw_input("Enter the lower limit: "))
b = int(raw_input("Enter the upper limit: "))
# Now, we initialize a counter to zero
n = 0
# We now check all the numbers between the intervals, including the intervals
for i in range(a, b+1):
    # We now initialize the divisors
    # We need to set the upper limit of the divisors to be NOT greater than the number itself, thus we divide it by 2
    for j in range(2, i/2):
        # If the remainder of the division is zero, it means that the number is not prime.
        # Thus, we will raise the counter to 1
        if i%j == 0:
            n = 1
            break
        # If the remainder is not zero, the counter is set at zero
        elif i%j != 0:
            n = 0
    # Finally, when the given number has been divided by all the possible divisors, we will check the counter again
    if n == 0:
        # We will print out the number as prime, if the counter value is zero
        print "%d is a prime number" % i
    elif n != 0:
        # If the counter value is not zero, we will print out the number as non-prime
        print "%d is not a prime number" % i
