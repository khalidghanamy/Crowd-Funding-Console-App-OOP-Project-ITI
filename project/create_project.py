def create_project(connection,project,user_email):
    data =True
    
    while True:
        

        
        
        title = input("Enter title : ")
        data = project.project_title(title)
        if data == False:
            continue
        details = input("Enter details : ")
        data = project.project_details(details)
        if data == False:
            continue
        total_target = input("Enter total_target : ")
        data = project.project_total_target(total_target)
        if data == False:
            continue
        start_time = input("Enter start_time : ")
        data = project.project_start_time(start_time)
        if data == False:
            continue
        end_time = input("Enter end_time : ")
        data = project.project_end_time(end_time)
        
        if data == False:
            continue
        else: 
            project.owner_email = user_email 
            
            project.project_id = project.project_id_generator(connection)
            
            break
        
    project_data = project.save_project()
    
    if project_data:
        print("created successfully ")
        connection.create(project_data)
        return True
        
    else:
        return False
    