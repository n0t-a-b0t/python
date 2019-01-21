listing = []
content_count = 0


def listops():
    global content_count
    content_count = int(raw_input("Enter the number of list contents: "))
    for i in range(0, content_count, 1):
        listing.append(raw_input("Enter list contents: "))
    return


def fileops():
    if not listing:
        print "No pre-built list exits. Create a list first!"
    else:
        filename_locate = int(raw_input("Enter the location of filename: "))
        filename_actual = filename_locate - 1
        fileobj = open(listing[filename_actual], 'w+')
        listing.pop(filename_actual)
        for i in range(0, content_count - 1, 1):
            fileobj.write(listing[i] + ' ')
        fileobj.close()
    return


def main():
    while True:
        operations = [listops, fileops]
        choice = int(raw_input("Enter choice: 1 - Populate list | 2 - Fileops: "))
        choice -= 1
        operations[choice]()
    return


main()
