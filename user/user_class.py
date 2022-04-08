
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
    
    def create_user(self,connection,user):

        
        data =True
        while True:

            
            
            name = input("Enter name : ")
            data = self.user_name(name)
            if data == False:
                continue
            name = input("Enter last name : ")
            data = self.user_last_name(name)
            if data == False:
                continue
            email = input("Enter email : ")
            data = self.user_email(email)
            if data == False:
                continue
            password = input("Enter password : ")
            confirm_password = input(" confirm password : ")
            data = self.user_password(password,confirm_password)
            if data == False:
                continue
            phone = input("Enter phone number : ")
            data = self.user_phone(phone)
            if data == False:
                continue
            else: 
                break
        
        user_data = self.save_user()
        if user_data:
            print("created successfully ")
            connection.create(user_data)
            return True
            
        else:
            return False
        