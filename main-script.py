import time
import datetime
import entry


def registration():
    f_name = entry.ask_for_name("first")
    l_name = entry.ask_for_name("last")
    email = entry.ask_for_email()
    password = entry.ask_for_password()
    phone = entry.ask_for_phone()
    id = round(time.time())
    data = f"{id}:{f_name}:{l_name}:{email}:{password}:{phone}\n"
    files_obj = open('data.txt', 'a')
    files_obj.write(data)
    files_obj.close()


def create_project(email_entry):  # for choice 1 (create project)

    title = entry.ask_for_title()
    details = entry.ask_for_details()
    total_target = entry.ask_for_target()
    start = entry.ask_for_date("start")
    end = entry.ask_for_date("end")

    id_project = round(time.time())
    project_data = f"{id_project}:{email_entry}:{title}:{details}:{total_target}EGP:{start}:{end}\n"
    project_obj = open('projects.txt', 'a')
    project_obj.write(project_data)
    project_obj.close()
    print("********-your project was saved successfully-**********")
    return project_data


def get_all_projects():
    projects_obj = open("projects.txt", "r")
    projects_data = projects_obj.readlines()
    projects_obj.close()
    return projects_data


def save_wanted_projects(projects):  # not used yet
    projects_obj = open("projects.txt", "w")
    projects_obj.writelines(projects)
    projects_obj.close()
    return True


def view_projects():  # for choice 2 (view all projects)
    print("====projects will be shown in the form (id:creator email:title:details:target:start date:end date)====")
    projects = get_all_projects()
    for project in projects:
        print(project)


def choose_the_edit():  # not yet configured right
    while True:
        wanted_item_to_change = input("(2)for name, (3)for details, (4)for target,(5)for start date, (6)for end date: ")
        if wanted_item_to_change != ("2" or "3" or "4" or "5" or "6"):
            continue
        elif wanted_item_to_change == "2":
            title = entry.ask_for_title()
            return title, 2
        elif wanted_item_to_change == "3":
            details = entry.ask_for_details()
            return details, 3
        elif wanted_item_to_change == "4":
            total_target = entry.ask_for_target()
            return total_target, 4
        elif wanted_item_to_change == "5":
            start = entry.ask_for_date("start")
            return start, 5
        elif wanted_item_to_change == "6":
            end = entry.ask_for_date("end")
            return end, 6


def edit_project(email_entry):  # for choice 3 (edit your own project)
    while True:
        wanted_id = input("""please enter the id of the project you want to edit:
         or you can go back by entering (0):  """)
        if wanted_id == "0":
            break
        projects = get_all_projects()
        for index, project in enumerate(projects):
            project_data = project.strip("\n")
            project_data = project_data.split(":")
            project_index = index
            if wanted_id == project_data[0]:
                if email_entry != project_data[1]:
                    print("--------THIS ISN'T YOUR PROJECT!. choose a project of yours to edit---------")
                    break
                else:
                    try:

                        edited_item, selected_item = choose_the_edit()
                        wanted_project = projects[project_index]
                        wanted_project_data = wanted_project.strip("\n")
                        wanted_project_data = wanted_project_data.split(":")
                        wanted_project_data[selected_item] = edited_item
                        wanted_project_data = ":".join(str(item) for item in wanted_project_data)
                        updated_project = wanted_project_data + "\n"
                        projects[project_index] = updated_project
                        edited = save_wanted_projects(projects)
                        if edited:
                            print("**********-project was edited successfully-***********")
                            break
                    except Exception as e:
                        print(e)
                        print("------------error occurred-------------")
        else:
            print("*********-this is not a current project, HERE is the list of projects again-********")
            continue


def delete_project(email_entry):  # for choice 4 (delete your own project)
    while True:
        wanted_id = input("""please enter the id of the project you want to delete:
         or you can go back by entering (0):  """)
        if wanted_id == "0":
            break
        projects = get_all_projects()
        for index, project in enumerate(projects):
            project_data = project.strip("\n")
            project_data = project_data.split(":")
            if wanted_id == project_data[0]:
                if email_entry != project_data[1]:
                    print("*******-THIS ISN'T YOUR PROJECT!. choose a project of yours to delete-******")
                    break
                else:
                    try:
                        # projects_obj_w = open("projects.txt", "w")
                        # for wanted_project in projects:
                        #     if wanted_id not in wanted_project:
                        #         projects_obj_w.writelines(project)
                        # projects_obj_w.close()
                        # print("_______________project was deleted successfully__________")
                        # break
                        del projects[index]   # if replaced add index and enumerate projects in above loop
                        deleted = save_wanted_projects(projects)
                        if deleted:
                            print("_______________project was deleted successfully__________")
                            break

                    except Exception as e:
                        print(e)
                        print("------------error occurred-------------")

        else:
            print("*********-this is not a current project-********")
            continue


def compare_date(num: int, date: str, type_of_date: str):  # to test if the project the user selects is his
    projects = get_all_projects()
    for project in projects:
        project_list = project.strip("\n")
        project_list = project_list.split(":")
        if date == project_list[num]:
            print(f"""_______project was found and here is its details_______
                    {project}""")
            continue
    else:

        print(f"________these are all the projects available now with such {type_of_date} date________")
        print("_________________if none were displayed then none were found_______________")


def search_by_date():  # for choice 5 (search in projects by date)
    while True:
        type_of_date = input("""please enter (start) for start date or (end) for end date
         oro you can enter (0) to go back""")
        if type_of_date.lower() != "start" and type_of_date.lower() != "end" and type_of_date != "0":
            continue
        else:
            while True:
                if type_of_date == "0":
                    break
                try:
                    date = input(f"please enter the {type_of_date.lower()} time of the project: ")
                    if date == datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'):
                        break
                    break
                except Exception:
                    print("______please enter the date in the format YY-mm-dd _____")
                    continue
            if type_of_date == "start":  # num=5 as index of start in the project list
                compare_date(5, date, type_of_date)
                break
            if type_of_date == "end":  # num=6 as index of start in the project list
                compare_date(6, date, type_of_date)
                break
            continue


def project_choice(email_entry):  # for user options after loging in
    while True:
        project_no = input("""please enter a number from 1 to 5: 
        1-----> create a new project 
        2-----> view all projects 
        3-----> edit your own projects 
        4-----> delete your own projects 
        5-----> search for a project using date 
        6-----> log out
        your choice:  """)
        if project_no == "1":
            create_project(email_entry)
        if project_no == "2":
            view_projects()
        if project_no == "3":
            edit_project(email_entry)
        if project_no == "4":
            delete_project(email_entry)
        if project_no == "5":
            search_by_date()
        if project_no == "6":
            break
        else:
            continue


def read_users_data():
    files_obj = open("data.txt", "r")
    files = files_obj.readlines()
    files_obj.close()
    return files


def password_logging(email_entry, selected_file):  # to check for password when logging in
    for i in range(3):
        password_entry = input("please enter your password: ")
        files = read_users_data()
        file = files[selected_file]
        file_data = file.split(":")
        password_known = file_data[4]
        if password_known == password_entry:
            print("_______logged in successfully______")
            project_choice(email_entry)
            break
        else:
            print("______password not correct______")
            continue


def logging():  # to check for email when logging in
    email_entry = input("please enter your email: ")
    files = read_users_data()
    for index, file in enumerate(files):
        file_data = file.split(":")
        email_known = file_data[3]
        if email_known == email_entry:
            password_logging(email_entry, index)
            break
    else:
        print("______email not found______")


def main_menu():  # for options in the main app screen
    while True:
        action = input("""________welcome to the funding app!______ 
        please enter 1 to register with a new account
                     2 to log in to your account  
                     3 to exit the app
        your choice:  """)
        if action == "1":
            registration()
        elif action == "2":
            logging()
        elif action == "3":
            break
        else:
            print("__________NOT EXPECTED ENTRY__________")
            continue


main_menu()
