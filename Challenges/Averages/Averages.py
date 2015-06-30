__author__ = 'Eugene'
import statistics

# Initialize starter number-holding list
numbers = []

# Check to see if there is a saved numbers text file. If not, create one.
try:
    with open("numbers.txt") as f:
        if input("Do you want to see your existing numbers? y/n ").lower() in ["y", "yes"]:
            print(f.read().strip("\n"))
except FileNotFoundError:
    with open("numbers.txt", "w") as f:
        print("There is currently no existing saved numbers file. One will be generated.")

while True:
    try:
        numbers.append(float(input("Please enter a number ")))
    except ValueError:
        print("Please enter a valid numerical value.")
        continue

    if input("Do you want to output the average? y/n ").lower() in ["y", "yes"]:
        print("The mean of the numbers entered so far is {}".format(statistics.mean(numbers)))
        print("The median of the numbers entered so far is {}".format(statistics.median(numbers)))
        try:
            print("The mode of the numbers entered so far is {}".format(statistics.mode(numbers)))
        except statistics.StatisticsError:
            print("There is no mode, all numbers input are equally common.")

    if input("Do you want to store your numbers in a text file? This will overwrite the existing file. y/n ").lower() in ["y", "yes"]:
        with open("numbers.txt", "w") as f:
            f.write(str(numbers))
            f.flush()

    if input("Do you want to quit the program? y/n ").lower() in ["y", "yes"]:
        exit()
