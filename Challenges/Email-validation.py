__author__ = 'Eugene'
def email_validation(email):
    errors = []

    [errors.append("An email cannot have a 
    if " " in email:
        errors.append("The email has whitespace")
    if "@" not in email:
        errors.append("The email does not have an @ character.")
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

    [errors.append("The domain name is invalid.") if item == "" for item in domain_name_list]
    
