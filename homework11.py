# Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:
s1 = {1, 2, 3, 4}
s2 = {2, 6, 11, 1}
union = s1.union(s2)
intersection =  s1.intersection(s2)
sym_diff = s1.symmetric_difference(s2)
print(f'Union: {union}\nIntersection: {intersection}\nSymmetric difference: {sym_diff}')




# Ստեղծել ծրագիր, որը կներառի օգտատերերի տվյալների ներմուծումը, պահպանումը բառարանում և ցուցակում, 
# ապա ցույց կտա օգտատերերին ըստ ներմուծված անվան(“Not found”, եթե այդպիսի օգտատեր գոյություն չունի)։
# Յուրաքանչյուր օգտատեր պետք է ունենա հետևյալ դաշտերը՝ ID, անուն, ազգանուն, Էլ. փոստ, գաղտնաբառ և հեռախոսահամար:
my_data = [{"ID":"123", "Name":"Ann", "Surname":"Dash", "Email":"anndash@gmail.com", "Password":"123qwe", "Phone number":"890978"},
           {"ID":"456", "Name":"Bob", "Surname":"Smith", "Email":"bobsmith@gmail.com", "Password":"456cvb", "Phone number":"453216"},
           {"ID":"789", "Name":"Kate", "Surname":"Scavo", "Email":"katescavo@gmail.com", "Password":"098klj", "Phone number":"765433"}]

while True:
    print("Choose")
    print("1. Register new user")
    print("2. Search user")
    print("3. Exit")

    choice = int(input("Enter choice 1, 2 or 3: "))

    if choice == 1:
        new_user = {}
        new_user["ID"] = input("Enter ID: ")
        new_user["Name"] = input("Enter name: ")
        new_user["Surname"] = input("Enter surname: ")
        new_user["Email"] = input("Enter email: ")
        new_user["Password"] = input("Enter password: ")
        new_user["Phone number"] = input("Enter phone number: ")
        my_data.append(new_user)
        print("Success")
    
    if choice == 2:
        search_name = input("Enter name: ").capitalize()
        flag = False
        for name in my_data:
            if name["Name"] == search_name:
                print(f"ID: {name['ID']}, Name: {name['Name']}, Surname: {name['Surname']}, Email: {name['Email']}, Phone Number: {name['Phone number']}")
                flag = True
        if not flag:
            print("There is no such user.")

    if choice == 3:
        print("Exiting...")
        break