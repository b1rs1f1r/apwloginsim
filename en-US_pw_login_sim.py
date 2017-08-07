for x in range(3):
    password=input("Enter a password: ")
    if x==2:
        print("You entered false password 3 times.",
        "Please try again later...")

    elif not password:
        print("Password can not void")

    elif len(password) in range(4,8):
        print("Your new password: ",password)
        break

    else:
        print("Password must be longer than 3 and shorter than 8 character")
