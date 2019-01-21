# Program to generate sum of all numbers up to a given number in Python
# We can do this by two way, 1: by using an iterator and 2: by using a generator
# Let's go to the main function and start from there...

# If the input was to implement without a generator, we will use an iterator to sum all numbers up to the
# inputted number


def without_gen():
    # We input the number till where we want the sum
    number = int(raw_input("Enter the number: "))
    # As range function does not include the upper limit in its operation, we will increment the inputted number by 1
    number += 1
    # We will create an output variable and initialise it to 0
    dildo = 0
    # We now implement the iterator and run it over the range 0 to number incrementing it by 1 for each iteration
    for i in range(0, number, 1):
        # We will add the iterator value to the value of the output variable
        dildo = dildo + i
    # Once the iteration is complete, we will print the value of the output variable
    print "sum of all numbers up to the given number is: ", dildo
    # We will return to the main() function
    return

# The generator function takes the inputted number as the input


def generatorfunct(number):
    # We will initialize a counter to 0 value
    flag = 0
    # We will create a while loop. Generally, all generators use a while loop
    # We will keep on checking it the value of the flag counter if it is greater than the inputted number
    while flag <= number:
        # We use yield to return the value of flag to the caller [sum()]
        # Yeild return the value to the sum() but does not stop the generatorfunct() function; rather it halts it.
        # Once the value if yielded, the function can resume its normal operation
        # Difference between yield and return is that 'return' returns a specific value and stops the function
        # and has to be called again.
        # The function runs from scratch when it is called again thus erasing the values of the old iteration
        # Yield halts a function so that it can resume its normal operation
        # Hence, yield is useful for returning a set / list of values WITHOUT storing all the values in the memory
        yield flag
        # We will increment 'flag' value by 1 for yielding the next number
        flag += 1
    # When the generatorfunct() function finishes execution, we return to the caller function
    return

# If we chose to use a generator, we will use the following function


def with_gen():
    # We inout the number form the user up to which we need the sum
    number = int(raw_input("Enter the number: "))
    # We will now use the in-built sum() function with the generator to calculate the sum
    # We will pass the value of the inputted number to the generator function

    # When the 'flag' value is yielded, the sum function will add the value to the already existing value
    print "Sum of all numbers up to the given number is: ", sum(generatorfunct(number))
    # Once we print the sum, we return to the main() function
    return

# The code execution starts from here


def main():
    # We create an infinite loop
    while True:
        # We create a list of operations to choose from
        operations = [without_gen, with_gen]
        # Now, we input the operation number to execute
        choice = int(raw_input("Enter your choice: 1: without gen | 2: with gen: "))
        # As the numbering in python starts from 0, we will decrease the operation number inputted by 1
        choice -= 1
        # Now, we choose the corresponding function
        operations[choice]()
    return


main()
