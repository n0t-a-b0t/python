# Program demonstrating the modular function of python
# Here, we will define two functions, one for inputting a string and another for printing it
# Let's start with the main function, so skip to the main function
# Here, we define main function with the def statement

# We will put a default value in the global variable in case task02 is executed before task01
mainstring = 'String not previously stored'

# Now, let's define the function for inputting the string


def task01():
    # Now, as we will be using the same variable for representing the string, we will define it as global variable
    # We need to explicitly define a global variable with the keyword global in python
    global mainstring
    # Now, let's input value from the user
    mainstring = (raw_input("Enter a string: "))
    return

# Now let's define a function for outputting the stored string


def task02():
    # Let's print the stored string
    print mainstring
    return


def main():
    # Now let's create a menu list for operation
    menulist = [task01, task02]

    # In order to make the program run in an infinite loop, we will use the while 'True' condition
    while(True):

        # Let's ask user to input the operation: 1 for input (task01) and 2 for output (task02)
        op = int(raw_input("Enter operation number: 1 for input and 2 for output: "))

        # Since counting in python starts from 0, we will need to reduce the input by 1
        # Alternatively, we can ask the user to input 0 for inputting the string and 1 for outputting the stored string
        op -= 1

        # Now, let's assign 'op' value to menulist for choosing the respective function
        menulist[op]()
    return


main()
