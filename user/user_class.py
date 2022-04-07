
import hashlib
import re

class User:

    def __init__(self,first_name = "",last_name = "", email = "",password = "",phone = ""):
        self.first_name= first_name
        self.first_name=last_name
        self.email=email
        self.password=password
        self.phone=phone

    def user_name(self,name):

            if name and name.isalpha():
                self.first_name = name
            else :
                print("name is not valid")
                return False
    
    def user_last_name(self,name):

            if name and name.isalpha():
                self.last_name = name
            else :
                print("name is not valid")
                return False
    
    def user_email(self,email):
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex,email):
            self.email= email 
        else :
            print("email is not valid")
            return False

    def user_password(self,password,confirm_password):
    
        if password and len(password) >= 8 and password == confirm_password:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.password =  hashed_password
        else :
            print("password is not valid")
            return False

    def user_phone(self,phone):
         
        regex = r'^01[0125][0-9]{8}$'
        if re.fullmatch(regex,phone):
            self.phone = phone 
        else :
            print("phone is not valid")
            return False

    def save_user(self):
        user = {
        "first_name_data" :self.first_name,
        "last_name_data" :self.last_name,
        "user_emaile_data": self.email,
        "user_password_data":  self.password,
        "user_phone_data":self.phone,
       
        }
        return user