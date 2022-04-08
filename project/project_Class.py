
from ast import literal_eval
from datetime import datetime



class Project:
    
    def __init__(self,project_id= 0,owner_email= "",title= "",details= "",total_target= "",start_time= "",end_time=""):
        self.project_id=project_id
        self.owner_email=owner_email
        self.details=details
        self.title=title
        self.total_target=total_target
        self.start_time=start_time
        self.end_time=end_time

    def project_title(self,title):

        
        if title and title.isalpha():
            self.title = title
        else :
            print("title is not valid")
            return False

    def project_details(self,details):
    
        if details and details.isalpha():
            self.details = details
        else :
            print("details is not valid")
            return False

    def project_total_target(self,total_target):

        if total_target and total_target.isnumeric():
            self.total_target = total_target
        else :
            print("total target is not valid")
            return False

    def project_start_time(self,time):
        format = "%H:%M:%S"
        
        if bool(datetime.strptime(time, format)):
            self.start_time = time
        else :
            print("time is not valid")
            return False
    
    def project_end_time(self,time):
        format = "%H:%M:%S"
        if bool(datetime.strptime(time, format)):
            self.end_time = time
        else :
            print("time is not valid")
            return False

    def save_project(self):
        project = {
        "project_id" :self.project_id,
        "owner_email": self.owner_email,
        "details":self.details,
        "title":self.title,
        "total_target":self.total_target,
        "start_time":self.start_time,
        "end_time" :self.end_time

        }
        return project
    
    def project_id_generator(self,connection):
        my_project_counters=connection.line_counter()
        
        
        if my_project_counters:
            return my_project_counters + 1
        else:
            return 0

    def get_all_data(self,connection,match):
        my_project = connection.file.readlines()

        counter = 0
        connection.file.seek(0)
        for line in my_project:
        
            data = literal_eval(line)
    
            if data["owner_email"] == match:
                counter+=1
                title = data["title"]
                project_id = data["project_id"]
                print(f"{counter}- title is {title} and id = {project_id} .")
        if counter ==0:
            print(" >>>>>  NO projects  <<<<<")
        return counter

    def edite_menu(self):

        title = ""
        details=""
        total_target=""
        start_time=""
        end_time=""

        menu_to_edite = """"

============
============>>>  UPDATE <<<============
============

1-title
2-details
3-total_target
4-start_time
5-end_time
6-close
    """
        print(menu_to_edite)
        while True:
            
            res = input(' select to edite : ')
            if res == "1" :
                title = input(' new title : ')
            elif res == "2" :
                details = input(' new details : ')
            elif res == "3" :
                total_target = input(' new total_target : ')
            elif res == "4" :
                start_time = input(' new start_time : ')
            elif res == "5" :
                end_time = input(' new end_time : ')
            elif res == "6" :
                break
    
        data = [title,details,total_target,start_time,end_time]
        return data

    def create_project(self,connection,user_email):
        data =True
        
        while True:
            

            
            
            title = input("Enter title : ")
            data = self.project_title(title)
            if data == False:
                continue
            details = input("Enter details : ")
            data = self.project_details(details)
            if data == False:
                continue
            total_target = input("Enter total_target : ")
            data = self.project_total_target(total_target)
            if data == False:
                continue
            start_time = input("Enter start_time : ")
            data = self.project_start_time(start_time)
            if data == False:
                continue
            end_time = input("Enter end_time : ")
            data = self.project_end_time(end_time)
            
            if data == False:
                continue
            else: 
                self.owner_email = user_email 
                
                self.project_id = self.project_id_generator(connection)
                
                break
            
        project_data = self.save_project()
        
        if project_data:
            print("created successfully ")
            connection.create(project_data)
            return True
            
        else:
            return False
        