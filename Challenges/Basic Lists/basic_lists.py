__author__ = 'Eugene'

has_names = False
input_required = True
input_first_received = False

while True:
    if has_names and input_first_received:
        if input("Do you want to use a new list of names? Otherwise the list in its current form will continue to" +
                         " be used. Y/N ").lower() in ["y", "yes"]:
            input_required = True
            input_first_received = False
        else:
            input_required = False
    if input_required:
        if input("Do you want to load up an existing file with a list of names in it? Y/N ").lower() \
                in ["y", "yes"]:

            filename = input("Please enter the filename of the file, including the extension: ")

            try:
                with open(filename) as f:
                    names = list(f)

                    names = [name.strip("\n") for name in names]
                    names = [name.strip() for name in names]
                    names = [name for name in names if name != ""]
                    has_names = True
                    input_first_received = True

            except FileNotFoundError:
                print("File doesn't exist in this directory.")
                continue

        else:
            names = input("Please enter a list of names in one line, separated by a comma: ").split(",")
            names = [name for name in names if name != ""]
            names = [name.strip() for name in names]
            if len(names) == 0:
                print("You didn't enter any names! Please try again.")
                continue
            has_names = True
            input_first_received = True

    print("What do you want to do with the list? Type the number for the right operation")
    print("1: Print out the list in original order")
    print("2: Print out the list in reverse order")
    print("3: Print out the (eg 3rd) name in the list.")
    print("4: Print out a portion of the list, eg the 1st to 4th item. (inclusive)")
    print("5: Remove a name from the list by providing the position of the name, or give a list of positions " +
          "for the names to be removed.")
    print("6: Save the list to a new or existing file.")
    print("7: Make all names in the list lowercase")

    operation = input("Choose operation number: ")  # Note operation is a string, not an int, so I don't have to write another try-catch block to catch a ValueError if the user has entered a non-numeric value. Instead, if the input doesn't match any of the above then it will just fall through to the else statement and the user will be notified so.

    if operation == "1":
        print(names)
        continue

    elif operation == "2":
        temp_names = []
        temp_names = names.copy()
        temp_names.reverse()
        print(temp_names)
        del temp_names
        continue

    elif operation == "3":
        while True:
            try:
                position = int(input("Please enter the position of the name you want to print: "))
            except ValueError:
                print("Make sure you enter a single number, with no decimal dots or extra non-numeric characters")
                continue

            try:
                print(names[position - 1])
                break
            except IndexError:
                print("Invalid position entered.")
                continue
        continue

    elif operation == "4":
        while True:
            try:
                positions = input("Please input the range of positions that you wish to print, separated by a comma." +
                                  "For example, if you want to print the 3rd, 4th and 5th names " +
                                  "enter \"3, 5\" ").split(",")
                if len(positions) != 2:
                    print("Please input 2 positions as specified!")
                    continue

                positions = [pos.strip() for pos in positions]
                positions = [int(pos) for pos in positions]
            except ValueError:
                print("Please input valid numerical values")
                continue

            try:
                positions = range(positions[0] - 1, positions[1])
                [print(names[pos]) for pos in positions]
                break
            except IndexError:
                print("Please input positions where names actually exist! For example, if your list has 5 names," +
                      " don't ask for the 6th through 8th names to be printed.")
                continue

    elif operation == "5":
        while True:
            try:
                positions = input("Please input the range of positions that you wish to remove, separated by a comma." +
                                  "\nFor example, if you want to remove the 3rd, 4th and 5th names enter \"3, 5\"." +
                                  "\nIf you want to remove a single item, then just input that single position." +
                                  "\n For example, if you want to remove the 5th name then input \"5\" ").split(",")
                if len(positions) > 2 or len(positions) < 1:
                    print("Please input 2 positions for a range, or one for a single value to be removed")
                    continue

                positions = [pos.strip() for pos in positions]  # remove whitespace
                positions = [int(pos) for pos in positions]  # position values to int
            except ValueError:
                print("Please input valid numerical values.")
                continue



            try:
                if len(positions) == 2:
                    positions = range(positions[0] - 1, positions[1])  # create range of positions from input args.
                    print(positions)
                else:
                    positions[0] -= 1

                [print("{} removed.".format(names.pop(positions[0]))) for i in range(len(positions))]
                break
            except IndexError:
                print("Please input positions where names actually exist! For example, if your list has 5 names," +
                      " don't ask for the 6th through 8th names to be removed.")
                continue

    elif operation == "6":
        if input("Would you like to create a new file to put the names in? Y/N ").lower() in ["y", "yes"]:
            filename = input("Please input the filename, including file extensions: ")
            try:
                with open(filename) as f:
                    overwrite = input("A file with that name already exists. Would you like to replace" +
                                      " it with the one you are making now? Y/N ").lower() in ["y", "yes"]
            except FileNotFoundError:
                with open(filename, "w") as f:
                    [f.write(name + "\n") for name in names]
                    f.flush()
                print("{} has been created and your list of names has been written to it.".format(filename))
                continue
            if overwrite:
                with open(filename, "w") as f:
                    [f.write(name + "\n") for name in names]
                    f.flush()
                    print("{} has been overwritten and your list of names has been written to it.".format(filename))
                    continue
            else:
                print("Operation canceled")
                continue
        else:
            filename = input("Please input the filename of a currently existing text file with a list of names you " +
                             "would like to add to: ")
            try:
                with open(filename, "a") as f:
                    f.writelines(names)
                    f.flush()
                print("Names successfully appended to existing file")
                continue
            except FileNotFoundError:
                print("The file specified could not be found in the working directory.")
                continue
    elif operation == "7":
        names = [name.lower() for name in names]
        print("All names made lower case.")

    else:
        print("Invalid operator")
