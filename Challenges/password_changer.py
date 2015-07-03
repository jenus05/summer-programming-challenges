import re, sqlite3

regex = re.compile("[\W]")

while (True):

    username1 = input("Please input a username")
    
    # Put code for searching for password username pair here
    oldpassword = input("Please input your old password")
    if (tablepassword != oldpassword):
        print("Your old password is wrong.")
        continue
    
    easywords = ["123456","password",username1]
    trustrating = 0
    password1 = input("Please enter a new password")
    for word in easywords:
        if (password1 == word):
            print("Your password is too common, or it is the same as your username.")
            continue
    
    
    if ((len(password1) >7) and ((password1.lower() or password1.upper()) != password1)):
        
        if (input("Thank you. Please enter your password again for verification purposes.") == password1):
            print("Thank you. Your password is now reset.")

            # Put code for setting the password here.
            

            if (len(password1) < 10):
                trustrating += 1
            elif (len(password1) < 12):
                trustrating += 2
            else:
                trustrating += 3

            m = regex.search(password1)
            if m:
                trustrating += 2
            print(trustrating)
            if (trustrating < 2):
                print("Your password is weak.")
            elif (trustrating < 4):
                print("Your password is medium strong.")
            else:
                print("Your password is very secure.")  
                
            break
        
        else:
            print("Your password does not match the first.")
            continue
        
    else:
        print("Your password needs to be at least 8 characters long and must have upper and lower case characters")
        continue

