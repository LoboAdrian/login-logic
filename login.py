import time

# New or returning user?
log = input(str("Create account?(y/n): "))


# Register your username and password, if a new user
def signup():
    write = open("signup.txt", "w")
    newuser = input(str("Username: "))
    newpass = input(str("Password: "))
    data = [newuser, newpass]
    for info in data:
        write.write(info + "\n")
    write.close()
    print("Signed up successfully")
    time.sleep(3)


# Check if your login info is correct, if a returning user
def logs():
    username = input(str("Username: "))
    password = input(str("Password: "))
    read = open("signup.txt", "r")
    # Turn the .txt file into a list
    r = read.readlines()
    newInfo = []
    for newData in r:
        newInfo.append(newData.strip())
    # If login info is correct
    if username == newInfo[0] and password == newInfo[1]:
        print("Logged In")
        time.sleep(3)
    # If login info is wrong
    else:
        print("Login failed")
        logs()


# New or returning user
if log == "y":
    signup()
else:
    logs()

