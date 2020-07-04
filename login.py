import time

log = input(str("Create account?(y/n): "))


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


def logs():
    username = input(str("Username: "))
    password = input(str("Password: "))
    read = open("signup.txt", "r")
    r = read.readlines()
    newInfo = []
    for newData in r:
        newInfo.append(newData.strip())
    if username == newInfo[0] and password == newInfo[1]:
        print("Logged In")
        time.sleep(3)
    else:
        print("Login failed")
        logs()


if log == "y":
    signup()
else:
    logs()
