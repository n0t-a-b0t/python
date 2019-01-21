# Program to demonstrate classes in Python
# Here, we will create a class 'Person' and enter information into it.
# We can then view the inputted information
# Let's create the class first


class person:
    # Now, we will define the __init__(self) function and let class person take in 4 arguments
    # 'self' parameter is executed by default and it does not need to be passed from the calling object
    # We can enter the default parameter values here, like height = 0.0...
    # Note that variables defined in a class are 'global' in that class
    # Meaning, if we had defined inputop() and outputop() inside class person, we wouldn't have to explicitly
    # define global variables
    def __init__(self, height, weight, hair_color, eye_color):
        self.hei = height
        self.wei = weight
        self.hc = hair_color
        self.ec = eye_color
        return


# We now define the default global variable values and pass them to the class with a globally defined object 'myself'
hei = ''
wei = ''
hc = ''
ec = ''
myself = person(hei, wei, hc, ec)
# Now, go to the main() function. We will start from there.....
# We will run the inputop() function if the user chose to input values


def inputop():
    # We specify that we are going to change the global variables
    global hei, wei, hc, ec, myself
    # We now input data from user
    hei = float(raw_input("Enter height (in cms): "))
    wei = float(raw_input("Enter weight (in lbs): "))
    hc = raw_input("Enter Hair Color: ")
    ec = raw_input("Enter Eye Color: ")
    # Now, we pass that data to the myself object which then uses class person to build itself
    myself = person(hei, wei, hc, ec)
    # We then return to the calling [main()] function
    return


# We will now use the outputop() function if the user chose to output the object values.
# Note that if no values are initially entered, the default values are displayed

def outputop():
    print "Here's the information you entered...."
    # We now print the corresponding object values.
    print "Height (in cms): ", myself.hei
    print "Weight (in lbs): ", myself.wei
    print "Hair Color: ", myself.hc
    print "Eye Color: ", myself.ec
    # Once the values are printed, we return to the calling [main()] function
    return


# Program execution will start from this function


def main():
    # We will create an infinite loop
    while True:
        # We will ask for the operation number from the user:-
        # 1 for input operation, 2 for output operation.
        # If the inputted number is something different, we will notify the user to input either 1 or 2
        choice = int(raw_input("Enter operation number: 1 - input | 2 - output: "))
        if choice == 1:
            # We will call the inputop() function if the user chose to input values
            inputop()
        elif choice == 2:
            # We will call the outputop() function if the user chose to print the object values
            outputop()
        else:
            print "Enter either 1 or 2, please..."
    return


main()
