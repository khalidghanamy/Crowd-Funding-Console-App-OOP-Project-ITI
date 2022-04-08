


from tabnanny import check
from venv import create
from login.login import login
from crud_menu.menu import menu
from user.user_class import User
from project.project_Class import Project
from connection.connectionClass import Data_base

project_database = f"C:\\Users\\user\\pythonClass\\Database\\projects.txt"
user_database = f"C:\\Users\\user\\pythonClass\\Database\\user_data.txt"




user_connection = Data_base(user_database)
project_connection = Data_base(project_database)
user = User()
project = Project()
def app(user_connection,project_connection,user,project):
    
    while True:
        logged = login(user_connection,user)
        if logged[0] :
            user_email = logged[1]
            menu(project_connection,user_email,project)
        else:
            check_user = input(">>>>  TRY Again (y) ?")
            if check_user == "y":
                continue
            else:
                print("""
                =====================
                >>>>>  GOOD BYE <<<<<
                =====================
                
                """)

                break
            

app(user_connection,project_connection,user,project)