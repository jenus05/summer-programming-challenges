__author__ = 'Eugene'
import random

# VARIABLES
random_number, input_number = "", ""  # random_number and input_number are treated as strings for ease of manipulation
try_count = 1  # The user will always take at least 1 try
correct_number_count = 0  # Per try, how many numbers are right


# File handling
try:
    with open("highscore.txt", "r") as f:
        highscore_data = list(f)
        print("The lowest number of tries was achieved by: {0} using only: {1} guesses"
              .format(highscore_data[0].strip("\n"), highscore_data[1]))
        highscore = int(highscore_data[1])
except FileNotFoundError:
    with open("highscore.txt", "w") as f:
        highscore = 0
        print("There is currently no highscore. Playing this for the first time will set the benchmark, so good luck!")

# Gamemode Selection
while True:
    gamemode = input("Please enter a gamemode. Choose from easy, normal or hard: ").lower()

    if gamemode not in ["easy", "normal", "hard"]:
        print("Gamemode not valid")
        continue

    if gamemode == "hard":
        max_numbers = 5
        break

    else:
        max_numbers = 4
        break

# Random number generation
for count in range(max_numbers):
    random_number += str(random.randint(0, 9))
    print(random_number)

# Game logic loop
while True:
    input_number = input("Please enter a {} digit number: ".format(max_numbers))

    try:
        input_number = int(input_number)
        input_number = str(input_number)
    except ValueError:
        print("Please ensure you enter a number, no letters.")
        continue

    if len(input_number) != max_numbers:
        print("please ensure you enter a {} digit number".format(max_numbers))
        continue

    if input_number == random_number:
        print("Congratulations! You found the right number! It took you ", try_count, " tries.")
        if highscore > try_count:
            name = input("Extra congrats! It seems you have the lowest number of guesses so far! Insert your word here: ")
            with open("highscore.txt", "w") as f:
                f.writelines([name + "\n", str(try_count)])
                f.flush()
        else:
            print("You unfortunately didn't get the highscore. Better luck next time.")
        exit()

    else:

        try_count += 1
        correct_number_count = 0
        correct_at_index = []

        for count in range(0, 4):
            if random_number[count] == input_number[count]:
                correct_number_count += 1
                correct_at_index.append(count + 1)
        print("You got {0} out of {1} numbers correct.".format(correct_number_count, max_numbers))
        if gamemode == "easy":
            print("You got the numbers right at positions: ", correct_at_index)
