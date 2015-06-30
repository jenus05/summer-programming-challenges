__author__ = 'Eugene'


def email_validation_format(email_input):
    if len(email_input) == 0:
            print("Please input an email!")  # I should really put this outside the function but my code is too complicated right now for me to bother. Either way it works here.
            return False
    def email_validation(email):

        errors = []

        if " " in email:
            errors.append("The email has whitespace")
        if "@" not in email:
            errors.append("The email does not have an @ character.")
            return [False, errors]
        if email.count("@") > 1:
            errors.append("The email has more than one @ character.")
            return [False, errors]

        email_list = email.split("@")

        if len(email_list[0]) == 0:
            errors.append("The email does not have a username.")
        if len(email_list[1]) == 0:
            errors.append("The email does not have a domain name")
            return [False, errors]

        domain_name = email_list[1]
        if "." not in domain_name:
            errors.append("The domain name is invalid, it doesn't have a period")
        else:
            domain_name_list = domain_name.split(".")

            temp_errors = []

            [temp_errors.append(
                "The domain name is invalid. " +
                "You cannot have a period as the first or last character of the domain name. ")
             for item in domain_name_list if item == ""]

            [errors.append(item) for item in temp_errors if item not in errors]

            del temp_errors

        user_name = email_list[0]

        if "." in user_name:
            temp_errors = []
            user_name_list = user_name.split(".")

            [temp_errors.append(
                "The user name is invalid." +
                " You cannot have a period as the first or last character of the user name.")
             for
             item in user_name_list if item == ""]
            [errors.append(item) for item in temp_errors if item not in errors]

            del temp_errors

        if len(errors) == 0:
            return [True, errors]
        else:
            return [False, errors]

    validation_metadata = email_validation(email_input)
    print("Email: {}".format(email_input.strip("\n")))
    if validation_metadata[0]:
        print("There are no problems identified.")
    else:
        print("Problems:")
        problems = validation_metadata[1]
        [print("\t", item) for item in problems if len(problems) != 0]
    print("")

while True:
    if input("Do you want to open a file with emails in? Y/N ").lower() in ["y", "yes"]:
        filename = input("Please input the name of the file containing the emails to be validated: ")
        try:
            with open(filename) as f:
                email_list = list(f)
                [email_validation_format(item.strip("\n")) for item in email_list if item.strip("\n") != ""]
        except FileNotFoundError:
            with open(filename, "w") as f:
                print("File was not found. One has been created in the same folder as this program: ")
    else:
        email_validation_format(input("Please enter an email to be validated:"))