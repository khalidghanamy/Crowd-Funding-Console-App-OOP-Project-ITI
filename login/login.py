    
from user.create_user import create_user


def login(user_connection,user):

    print("""
========================
>> USER MENU :
========================

1- LOIGIN
2- REGISTER
3- Exit 
------------------------ 
    """)
    while True:
    
        res = input("--> select from menu : ")
        logged = [False,"",""]
        if res == "1":
            user_email = input(" user email : ")
            user_password = input(" user password : ")
            logged = user_connection.check_login(user_password,user_email)
            
            if logged:
                
                logged = [True,user_email,user_password]
                break
            else:
                continue
        if  res == "2":
            registered = create_user(user_connection,user)
            if registered:
                
                print(" go to login ==> ")
                continue
            else:
                continue
        if res == "3":
            logged = [False,"",""]
            break
        else:
            continue
    return logged     