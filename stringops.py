# Program explaining string operations
# Let's use a string list

callsign = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']

# Now, we will print only the FIRST 3 characters of the contents

print "First 3 characters of all entries in the list\n"
for i in callsign:
    print i[0:3]

# This print statement only goes over the FIRST 3 CHARACTERS of the list entries
# Now, let's print all the entries backwards

print "\nAll entries backwards\n"
for i in callsign:
    print i[::-1]

# The [::] indicates that we are including all characters of the entry from left to right
# The -1 in [::-1] indicates that all characters in the entries are being considered backwards, i.e. from right to left
