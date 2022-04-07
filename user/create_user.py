


def create_user(connection,user):

    
    data =True
    while True:

        
        
        name = input("Enter name : ")
        data = user.user_name(name)
        if data == False:
            continue
        name = input("Enter last name : ")
        data = user.user_last_name(name)
        if data == False:
            continue
        email = input("Enter email : ")
        data = user.user_email(email)
        if data == False:
            continue
        password = input("Enter password : ")
        confirm_password = input(" confirm password : ")
        data = user.user_password(password,confirm_password)
        if data == False:
            continue
        phone = input("Enter phone number : ")
        data = user.user_phone(phone)
        if data == False:
            continue
        else: 
            break
    
    user_data = user.save_user()
    if user_data:
        print("created successfully ")
        connection.create(user_data)
        return True
        
    else:
        return False