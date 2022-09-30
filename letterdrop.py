# This coverts the user's string input to a list because strings are immutable and cannot be changed.
# Lists can be changed and then converted back to strings. 

## helper functions

def convert_string_to_list(entry):
    li = list(entry)
    # remove blanks in list
    # return items (i) for index (spot #), item in enumerate(listname) when i is not equal to blank
    # list comprehension and shorter way of saying:
    # for a, i in enumerate(listname):
        # if i != ' '
        # return i (only non blank list items are returned)
        # in list ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'], 
        # the blank in index/enumerate spot 5 (remember 0 indexing) is blank, so it will be dropped
        # and you're left with ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    new_li = [i for a,i in enumerate(li) if i!=' ']
    return new_li

def convert_list_to_string(newList):
    st = ' '.join(newList)
    return st
    


# main function 
def main():

    entry = input("Enter a value: ")

    # convert the entry into separate letters into a list
    newList = convert_string_to_list(entry)
    # uncomment the print function below to see your entry printed as a list of separate letters
    # print("New List: ", newList)


    while len(newList) > 0:

        value = input("Enter character to remove from string: (type 'quit' to quit): ")

        # user option to quit
        # since "quit" is not an item in the list, this has to be first in the loop
        # otherwise, it will not find "quit" as a list item and will error or hit the 
        # elif below where it returns "Value not in list. Try again."
        if value == "quit":
            print("Closing program...")
            exit() 
        elif value in newList:
            # remove the value from the list
            newList.remove(value)
            # uncomment the print function below to see the value (letter) removed from the list
            # print("Updated list: ", newList)
            # convert list back to string
            newString = convert_list_to_string(newList)
            # print your updated string minus a value (letter)
            print("Updated string: ", newString)
            # in while loop, will continue to prompt for values to remove until the list is empty or user quits
            continue
        elif value not in newList:
            print("Value not in list. Try again.")
            continue
    # Nicer way to close the program when the where clause has been met in the loop (when string and list have 0 chars).
    print("String is empty. Closing app...")

if __name__ == '__main__':
    main()



