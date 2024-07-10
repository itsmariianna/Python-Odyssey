my_data = []
while True:
    print("\nChoose")
    print("1. Register new users")
    print("2. Full list")
    print("3. Search by name")
    print("4. Exit")

    choice = int(input("Enter choice 1, 2, 3 or 4: "))

    

    if choice == 1:   
        sum_users = int(input("Enter how many users you want to have: "))
        
        for i in range(1, sum_users + 1):
            print(f"Data for user {i}")
            id = input("Enter ID: ")
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone_number = input("Enter phone number: ")

            user_data = {
                'ID' : id,
                'Name' : name,
                'Surname' : surname,
                'Email' : email,
                'Password' : password,
                'Phone number': phone_number
            }

            my_data.append(user_data)


    if choice == 2:
        if len(my_data) == 0:
            print("Your data is empty. Choose 1 to enter users")
        else:
            print("Your users")
            for person in my_data:
                print(f"ID:{person['ID']}, Name:{person['Name']}, Surname:{person['Surname']}, Email:{person['Email']}, Passowrd:{person['Password']}, Phone number:{person['Phone number']}")


    if choice == 3:
        search_name = input("Enter name: ").capitalize()
        flag = False
        for name in my_data:
            if name["Name"] == search_name:
                print(f"ID: {name['ID']}, Name: {name['Name']}, Surname: {name['Surname']}, Email: {name['Email']}, Phone Number: {name['Phone number']}")
                flag = True
        if not flag:
            print(f"There is no such user. Choose 1 to enter user with name {search_name}")


    if choice == 4:
        print("Exiting...")
        break