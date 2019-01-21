# Program to implement sorting in Python
#
#
# Back-Tracking..........
# Word     :                    ABC
#
# 1st level:      A              B               C
#               A is fixed     B is fixed      C is fixed
#              /  \             / \           /   \
#             /    \           /   \         /     \
# 2nd level: ABC    ACB     BAC     BCA     CAB     CBA
#           Once we get to the rightmost characters, we will generate their permutations
# This concept is same for any word length
#
# In this program, we will input a word from the user
# Then, we will generate a list of all possible permutations of the letters in the entered word
# Finally, we will output the next list element of the entered word
# As in we are going to output the next lexicographic superior to the entered word
# Go to the main() function. Program execution starts there...

# This function generates all the permutations
# We will pass three (3) parameters from the main() function: 1 - auxiliary list, 2 - the left limit (initially
# zero (0)) and 3 - the right limit (initially the length of the auxiliary list)
# Refer the backtrack concept up top


def generator(ar_aux, left, right):
    # We check if the left and right limits match up
    if left == right:
        # If they do, we are going to enter the permutation into the main list
        ar_main.append(''.join(ar_aux))
    # If they aren't we will generate the permutation
    else:
        # Now, from the left limit to the right limit, starting from the top, we are fixing the positions of
        # the leftmost characters
        for i in xrange(left, right+1):
            ar_aux[left], ar_aux[i] = ar_aux[i], ar_aux[left]
            # We will use the same generator function to get the rightmost characters
            generator(ar_aux, left+1, right)
            # Once we get to the rightmost characters, we will generate their permutations
            ar_aux[left], ar_aux[i] = ar_aux[i], ar_aux[left]
    # When all the permutations are done, we will return to the calling [main()] function
    return

# This function is called to print the lexicographically superior permutation
# We will pass the inputted word from the main() function


def outputop(word_pass):
    # We will use the sort() function to rearrange the list in ascending order
    ar_main.sort()
    # We will now get the length of the main list
    m = len(ar_main)
    # Now, we will need to use the try - except block for handling exceptions
    try:
        # Going over all the contents of the main list
        for i in xrange(m):
            # If we get a match of the inputted word in the list, we will first do a check if it the last entry
            if word_pass == ar_main[i]:
                # If it isn't, we are good
                if not ar_main[i+1]:
                    print "No output"
                # If the matched entry is the same as the next entry, do a 'pass' (aka nop()) and execute the
                # next iteration
                elif ar_main[i] == ar_main[i+1]:
                    pass
                # If the above conditions do not match, we have our output and we will print it
                else:
                    print "The next permutation lexicographically is: ", ar_main[i+1]
    # We will handle exceptions with the except block
    except:
        print "There is no lexicographic superior"
    # Once this is done, we will return to the calling [main()] function
    return

# The program execution starts here


def main():
    # We will create a global list and initialize it as a null list
    global ar_main
    ar_main = []
    # Then we will input the 'word' from the user
    word = str(raw_input("Enter your word: "))
    # Next, we will get the length of the inputted word as well as split the word into individual characters and put
    # them into an auxiliary list
    n = len(word)
    n -= 1
    ar_aux = list(word)
    # Now, we will use two functions, one for generating all the permutations and another for getting the
    # lexicographically superior word

    # Let's get all the permutations
    generator(ar_aux, 0, n)
    # Once the permutations are generated, we will get the output
    outputop(word)
    return


main()
