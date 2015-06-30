__author__ = 'Eugene'


def email_validation(email):

    from re import compile, fullmatch
    errors = []
    VALID_CHARACTERS_REGEX = compile()

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
        return [False, errors]

    domain_name_list = domain_name.split(".")

    temp_errors = []

    [temp_errors.append(
        "The domain name is invalid. You cannot have a period as the first or last character of the user name. ") for
     item in domain_name_list if item == ""]
    [errors.append(item) for item in temp_errors if item not in errors]

    del temp_errors

    user_name = email_list[0]

    if "." in user_name:
        temp_errors = []
        user_name_list = user_name.split(".")

        [temp_errors.append(
            "The user name is invalid. You cannot have a period as the first or last character of the user name.") for
         item in user_name_list if item == ""]
        [errors.append(item) for item in temp_errors if item not in errors]

        del temp_errors

    if len(errors) == 0:
        return [True, errors]
    else:
        return [False, errors]


print(email_validation("@@website.com.com.."))
