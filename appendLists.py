
# This program uses two functions to
# append one list to another &
# prints the result.


# Function appends one list after another.
def appendList(listA,listB):
    # Create new conjoined list.
    listC = []
    # Link two lists.
    listC = listA + listB
    for elements in listC:
        print(elements,end="  ")

# Initializes lists.
def main():
    # Create List A & B
    listA = [1,4,9,16]
    listB = [9,7,4,9,11]
    # Call function.
    listC = appendList(listA,listB)


main()
