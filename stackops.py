# Stack implementation in Python
# In this program, we will implement class 'Stack' and push and pop content into and from it
# Let's define class 'Stack' first


class Stack:
    # We define the __init__() function
    # This function is executed when Stack is initialised
    def __init__(self):
        self.items = []

    # We define a function that will return 'True' if the Stack is empty
    def isEmpty(self):
        return self.items == []

    # We define a function to 'push' the contents onto the Stack
    def push(self, item):
        self.items.append(item)

    # Now, we define a function to 'pop' the most recent entry from the Stack
    def pop(self):
        return self.items.pop()


# This function checks if the entered string of parenthesis is 'balanced' or not
# A 'balanced' string is one in which every opening parenthesis has its respective closing parenthesis
# For example: ([{}]) is a balanced string whereas {(] is not
def Checker(symbolString):
    # We now create an object using class Stack
    s = Stack()

    balanced = True
    index = 0
    # While 'index' is less than the length of the string and 'balanced' is 'True', we will execute the following loop
    while index < len(symbolString) and balanced:
        # Let's consider the individual contents of the string
        symbol = symbolString[index]
        # If the character is an opening parenthesis, 'push' is to the Stack
        if symbol in "([{":
            s.push(symbol)
        # Else, first check if the Stack is empty
        else:
            # If it is, then change the value of 'balanced' to 'False'
            if s.isEmpty():
                balanced = False
            # If the Stack is not empty, then 'pop' the most recent entry from the stack and compare it to the current
            # character
            else:
                top = s.pop()
                # We will use another function (matches()) for doing the comparison
                # If the value returned is 'False', then change the value of 'balanced' to 'False'
                if not matches(top, symbol):
                    balanced = False
        # Increment 'index' by 1
        index = index + 1
    # Now, if the value of 'balanced' is 'True' after the end of the loop and if the Stack is empty, return 'True'
    if balanced and s.isEmpty():
        return True
    # Else, return 'False'
    else:
        return False


# This function does the matching between the current character in the loop to the recent value 'popped' from the Stack
def matches(open, close):
    # Let's define two strings that have corresponding opening and closing parenthesis
    opens = "([{"
    closers = ")]}"
    # Now, if the current character matches the recently 'popped' character, return 'True', else return 'False'
    return opens.index(open) == closers.index(close)


def main():
    # We will use an infinite loop
    while True:
        # We will input the string from the user
        input_string = str(raw_input("Enter parenthesis here: "))
        # We will then send it to Checker() function to see if it is 'balanced' or not
        # If it is, we will print 'True', else 'False'
        print(Checker(input_string))
    return


main()
