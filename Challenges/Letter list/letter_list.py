__author__ = 'Eugene'

while True:
    letter = input("Please input a letter: ").lower()
    # print(letter)

    if len(letter) != 1:
        print("Ensure you input a single character. Please try again.")
        continue

    else:
        print("Thank you.")

    if input("Do you want to load up an existing file with a list of words in it? Y/N ").lower() in ["y", "yes"]:
        filename = input("Please enter the filename of the file, including the extension: ")

        try:
            with open(filename) as f:
                words = list(f)
                # words = [word.strip("\n") for word in words]
                # words = [word.strip() for word in words]
                # words = [word for word in words if word != ""]
                # words = [word.lower() for word in words]
                # Combine list comprehensions into single one for efficiency
                words = [word.strip("\n").strip().lower() for word in words if word != ""]

                if len(words) == 0:
                    print("No words found!")
                    continue

        except FileNotFoundError:
            print("File doesn't exist in this directory.")
            continue

    else:
        words = input("Please enter a list of words in one line, separated by a comma: ").split(",")
        # words = [word for word in words if word != ""]
        # words = [word.strip() for word in words]
        # words = [word.lower() for word in words]
        # Combine list comprehensions into single one for efficiency
        words = [word.strip().lower() for word in words if word != ""]

        if len(words) == 0:
            print("You didn't enter any words! Please try again.")
            continue

    print("1. You can either choose to see the words beginning with your letter ")
    print("2. or the words where your letter is found at any position in the word.")

    operation = input("Enter either 1 or 2: ")

    if operation == "1":
        [print(word) for word in words if word[0] == letter]

    elif operation == "2":
        [print(word) for word in words if letter in word]

    else:
        print("Invalid selection.")
        continue
