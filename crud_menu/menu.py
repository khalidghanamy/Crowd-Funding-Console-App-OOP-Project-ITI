
from connection.connectionClass import Data_base
from project.create_project import create_project
from project.project_Class import Project
crud_minu_list = """ 
====================
CRUD MENU
====================

1-view all projects : 
2-create a project : 
3-edit project : 
4-delete project : 
5-search for a project : 
6-close menu : 


"""


def menu(connection,user_email,project):
    
    minu = ["1", "2", "3", "4", "5", "6"]
    while True:
        print(crud_minu_list)

        res = input("select from list : ")

        if res in minu:
            if res == "1":
                print(user_email)
                project.get_all_data(connection,user_email)
            if res == "2":
                create_project(connection,project,user_email)
            if res == "3":
                projects_number= connection.get_all_data(user_email)
                project_id = input("enter project id to edite  : ")
                if project_id <= projects_number and project_id >0:
                    data = project.edite_menu()
                    connection.edite(user_email,project_id,data[0],data[1],data[2],data[3],data[4])                
                
            if res == "4":
                
                project.get_all_data(connection,user_email)
                project_id = input("enter project id to delete  : ")
                connection.delete(user_email,project_id)

            if res == "5":
                title = input(" Enter title : ")
                connection.search(user_email,title)

            if res == "6":
                break
        else:
            continue
    return 1
