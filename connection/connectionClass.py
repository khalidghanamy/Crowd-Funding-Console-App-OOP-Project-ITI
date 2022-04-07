
from ast import literal_eval
import hashlib



class Data_base:
    
    def __init__(self,file_path):
        self.file= open(file_path,"r+")
        self.file_append = open(file_path,"a")
        

    def check_login(self,password,email):
       
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        my_data = self.file.readlines()
        flag = False
        for line in my_data:
            data = literal_eval(line)
            
            if data["user_password_data"] == hashed_password and data["user_emaile_data"] == email:
                flag = True

        return flag

    def create(self,data):
        self.file_append.write(f"{str(data)}\n")
        
        
    def delete(self,email,project_id):
        my_project = self.file.readlines()
        self.file.seek(0)
        for line in my_project:
            data = literal_eval(line)
            if data["owner_email"] == email and data["project_id"] == int(project_id):
                pass
            else:
                self.file.write(line)
        self.file.truncate()

    def edite(self,logged_user,id,title="",details="",total_target="",start_time="",end_time=""):
        my_project = self.file.readlines()
        
        str1 = ''.join(my_project)
        fixed_data=str1.split("\n")
        for index,line in enumerate(my_project) :
            data = literal_eval(line)
            
            if data["owner_email"] == logged_user and data["project_id"] == int(id):

                if title:
                    data['title'] = title
                    fixed_data[index]=str(data)
                    
                if details:
                    data['details'] = details
                    fixed_data[index]=data
                    
                if total_target:
                    data['total_ordering'] = total_target
                    fixed_data[index]=data
                    
                if start_time:
                    data['start_time'] = start_time
                    fixed_data[index]=data
                    
                if end_time:
                    data['end_time'] = end_time
                    fixed_data[index]=data
        
        for index,line in enumerate(fixed_data):
            if index==0:
                self.file.truncate(0)
                self.clear_file()
            
            self.file.write(f"{str(line)}\n")


    def search(self,logged_user,title):
        my_project = self.file.readlines()
        counter = 0
        self.file.seek(0)
        for line in my_project:
        
            data = literal_eval(line)

            if data["owner_email"] == logged_user and data["title"] == title:

                counter +=1
                title = data["title"]
                project_id = data["project_id"]
                print(f"{counter}- title is {title} and id = {project_id} .")
            
        if counter == 0:
            print("not found")

    def clear_file(self):
        lines= self.file.readlines()
        
        self.file.seek(0)
        for line in lines:
            if "\x00" in line:
                pass
            else:
                self.file.write(line)
        self.file.truncate()

    def line_counter(self):
        my_project = self.file.readlines()
        counter = 0
        self.file.seek(0)
        for line in my_project:
            counter += 1
        return counter
        
    # def get_all_data(self,match):
    #     my_project = self.file.readlines()

    #     counter = 0
    #     self.file.seek(0)
    #     for line in my_project:
        
    #         data = literal_eval(line)
    
    #         if data["owner_email"] == match:
    #             counter+=1
    #             title = data["title"]
    #             project_id = data["project_id"]
    #             print(f"{counter}- title is {title} and id = {project_id} .")
    #     if counter ==0:
    #         print(" >>>>>  NO projects  <<<<<")
    #     return counter



# connection.create({'project_id': 4, 'owner_email': 'kh@kh.cc', 'title': 'sssssssssssssssss', 'details': 'khalid', 'total_target': '1500', 'start_time': '10:20:10', 'end_time': '10:20:20'})
# connection.delete('kh@kh.cc',"2")
# connection.search('kh@kh.cc',"ppp")
# connection.edite('kh@kh.cc',"2","111111111111111","44")

# password = "15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225"
# email =  "kh@kh.cc"
# connection.check_data(password,email)

