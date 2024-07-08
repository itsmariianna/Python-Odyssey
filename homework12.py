print("REGISTRATION")

# Username
while True:
    username = input("Enter username: ")
    reserved_names = ['admin', 'root', 'username', 'supervisor', 'password']
    if not username.isalnum():
        print("Invalid username. Username should contain only alphanumeric characters.")
        continue
    if 5 > len(username) or len(username) > 20:
        print("Invalid username. Username should be between 5 and 20 characters long.")
        continue
    if username.lower() in reserved_names:
        print("Invalid username. This is a reserved name. Choose another username.")
        continue
    break
print("Success")


# Email
while True:
    email = input("Enter email: ")
    if email.count('@') != 1 or email.count('.') < 1:
        print("Invalid email. Try again.")
        continue
    break
print("Success")


# Phone
while True:
    phone = input("Enter phone number: ")
    if not ((phone[0:4] == '+374' and len(phone) == 12) or (phone[0] == '0' and len(phone) == 9)):
        print("Should be in a valid format (+374XXXXXXXX or 0XXXXXXXX).")
        continue
    break
print("Success")


# Password
while True:
    password = input("Enter password: ")

    upper = True
    lower = True
    digit = True
    special = True

    special_char = set("!@#$%^&*+?/><")

    for i in password:
        if i.isupper():
            upper = False
        elif i.islower():
            lower = False
        elif i.isdigit():
            digit = False
        elif i in special_char:
            special = False

    if upper or lower or digit or special or len(password) > 8:
        print("Invalid password. Password should be at least 8 characters long and must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*+?/><)")
        continue
    break
print("Success")


# Password repeat
while True:
    rep_password = input("Repeat password: ")
    if password != rep_password:
        print("Wrong. Should match the initially provided password.")
        continue
    break
print("Success")








