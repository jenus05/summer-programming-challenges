import re

regex = re.compile("[\W]")

while (True):

    username = input("Please input a username: ")

    # Declare variables here to bring them outside scope of the file-handling block for use later
    username_list, password_list, user_data_list = [], [], []
    table_password = 0

    
    # Put code for searching for password username pair here
    try:
        with open("userdata.txt", "r") as user_data: # Convert userdata.txt into two separate lists for usernames and passwords
            user_data_list = list(user_data)
            user_data_list = [item.strip("\n") for item in user_data_list] # Get rid of newline characters
            for item in user_data_list:
                if user_data_list.index(item) % 2 == 0:
                    username_list.append(item)
                else:
                    password_list.append(item)

            if username in username_list:
                table_password = password_list[username_list.index(username)]
            else:
                print("Username not found. Please try again.")
                continue
    except FileNotFoundError:
        print("userdata.txt cannot be found in the working directory. Program will exit.")
        exit()


    old_password = input("Please input your old password")
    if table_password != old_password:
        print("The password that you have just entered does not match the one currently associated with your username.")
        continue
    
    easy_words = ["123456","password", username]
    trust_rating = 0
    new_password = input("Please enter a new password")
    for word in easy_words:
        if (new_password == word):
            print("Your password is too common, or it is the same as your username.")
            continue
    
    
    if ((len(new_password) >7) and ((new_password.lower() or new_password.upper()) != new_password)):
        
        if (input("Thank you. Please enter your password again for verification purposes.") == new_password):
            print("Thank you. Your password is now reset.")

            # Put code for setting the password here
            password_list[username_list.index(username)] = new_password
            with open("userdata.txt", "w") as user_data:
                for count in range(len(username_list)):
                    user_data.write(username_list[count] + "\n")
                    user_data.write(password_list[count] + "\n")
                user_data.flush()

            

            if (len(new_password) < 10):
                trust_rating += 1
            elif (len(new_password) < 12):
                trust_rating += 2
            else:
                trust_rating += 3

            m = regex.search(new_password)
            if m:
                trust_rating += 2
            print(trust_rating)
            if (trust_rating < 2):
                print("Your password is weak.")
            elif (trust_rating < 4):
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

