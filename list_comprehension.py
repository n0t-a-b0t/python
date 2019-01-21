# Program explaining list comprehension in Python
# Let's input the x, y and z co-ordinates such that x+y+z != n
# There are two ways to do this... using nested for loops or by using list comprehension
# Go to the main function. Program execution starts from there...

# This function will be called if the use chose one (1)...


def non_list_comprehension():
    # We input values from the user for x, y, z and n
    x = int(raw_input("x: "))
    y = int(raw_input("Y: "))
    z = int(raw_input("Z: "))
    n = int(raw_input("N: "))
    # We create a null list
    ar = []
    # We increment values of x, y and z by one (1) for 'for' loop operations
    x += 1
    y += 1
    z += 1

    # We generate nested for loops for generating [i, j, k] for all values of i, j and k
    for i in range(0, x):
        for j in range(0, y):
            for k in range(0, z):
                # We check the condition: i+j+k != n
                if i+j+k != n:
                    # If the condition is satisfied, we will input the values in a temporary list, will will append
                    # the values to the actual list
                    si = [i, j, k]
                    ar.append(si)
    # Now, we print the actual list
    print ar
    return

# This function will be executed if the user chose two (2)...


def list_comprehension():
    # We will input values from the user for x, y, z and n
    x = int(raw_input("x: "))
    y = int(raw_input("Y: "))
    z = int(raw_input("Z: "))
    n = int(raw_input("N: "))
    # We will increment the values of x, y and z by one (1) for 'for' loop operations
    x += 1
    y += 1
    z += 1

    # List comprehension is a concise way of writing lists
    # It uses a print, append or similar operations followed by one or more for loops and if statements
    print [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]
    return

# The program execution starts from here


def main():
    # We create an infinite loop
    while True:
        # We create a list of function names and ask the user to choose one of them
        ar_main = [non_list_comprehension, list_comprehension]
        choice = int(raw_input("Enter 1 for non list comprehension, 2 for list comprehension: "))
        # Since the numbering in Python starts from zero (0), we will reduce the user choice value by one (1)
        choice -= 1
        # Now, we choose the respective function
        ar_main[choice]()
    return


main()
