session_numbers = []
lower_bound = 0.0
upper_bound = 0.0

while True:  # Set the minimum and maximum values
    try:
        lower_bound = float(input("Please enter the minimum value allowed for this instance of the program: "))
        upper_bound = float(input("Please enter the maximum value allowed: "))

        if upper_bound < lower_bound:
            print("Your maximum value cannot be lower than your minimum value. Please try again.")
            continue

        print("Thank you. Maximum and minimum values set successfully.")
        break

    except ValueError:
        print("Please enter a valid numerical value.")
        continue

while True:
    if len(session_numbers) != 0:
        print("The highest number entered is:", max(session_numbers))
        print("The lowest number entered is", min(session_numbers))
        print(len(session_numbers), "numbers entered so far.")

    else:
        print("There is currently no highest and lowest number entered because no values have yet been entered.")

    print("You have 3 options:\n")
    print("\tType \"save\" to save the numbers entered in this session. The current save file will be overwritten.\n")
    print("\tType \"recall\" to see the numbers in your save file.\n")
    print("\tOtherwise enter a number to add to the current session.")

    option = input(
        "save/recall/<number>: ")

    if option.lower() == "save":
        if len(session_numbers) == 0:
            print("You haven't entered any numbers this session. Save process aborted.")

        else:
            try:
                with open("numbers.txt", "w") as f:
                    for number in session_numbers:
                        f.write(str(number) + "\n")

                    f.flush()
                    print("Numbers saved successfully.")
                    continue

            except FileNotFoundError:
                with open("numbers.txt", "w") as f:
                    print("There is currently no existing saved numbers.txt file. One will be generated.")
                    continue

    elif option.lower() == "recall":
        try:
            with open("numbers.txt") as f:
                recall_numbers = list(f)  # turns file object into easier to handle list
                recall_numbers = [number for number in recall_numbers if
                                  number.strip("\n") != ""]  # removes empty values from list
                recall_numbers = [number.strip("\n") for number in recall_numbers]  # strips newline characters
                recall_numbers = [number for number in recall_numbers if
                                  lower_bound <= float(number) <= upper_bound]  # removes numbers

                if len(recall_numbers) == 0:
                    print(
                        "There are no numbers within the maximum and minimum values set saved in numbers.txt.")
                    continue

                for count in range(len(recall_numbers)):
                    if count + 1 != len(recall_numbers):
                        print(recall_numbers[count], end=", ")

                    else:
                        print(recall_numbers[count])

        except FileNotFoundError:
            with open("numbers.txt", "w") as f:
                print("There is currently no existing saved numbers.txt file. One will be generated.")

    else:
        try:
            option = float(option)

            if upper_bound >= option >= lower_bound:
                session_numbers.append(option)

            else:
                print(
                    "The number entered is outside the maximum and minimum values you have set. Number discarded.")

        except ValueError:
            print("Please enter a valid numerical value.")
            continue
