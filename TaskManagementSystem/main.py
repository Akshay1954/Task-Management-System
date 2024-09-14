from auth.auth import login_user, sign_up
from tasks.task_manager import add_task, remove_task, update_tasks, get_task

def main():
    print("Welcome to Task Manager")
    while True:
        action = input("Choose action: [register/login/exit]: ").strip().lower()
        if action == "register":
            username = input("Enter username : ")
            password = input("Enter password : ")
            if sign_up(username=username, password=password):
                print("User Registered Successfully")
            else:
                print("Name username already exists")
        
        elif action == "login":
            username = input("Enter username : ")
            password = input("Enter password : ")
            user_id = login_user(username=username,password=password)
            if user_id:
                user_interface(user_id=user_id)
            else:
                print("Invalid Credentials")
        elif action == "exit":
            print("Thank you for using our app!")
            break


def user_interface(user_id):
    while True:
        query = input("1) add a task\n2) remove task\n3) update task\n4) display tasks\n5) logout")
        if query == "1":
            title = input("Title : ")
            descr = input("Description : ")
            add_task(user_id=user_id, title= title, description=descr)
            print("Task Added")
        
        elif query == "2":
            id = int(input("Enter the task id : "))
            remove_task(task_id=id)
            print("Task removed successfully")
        elif query == "3":
            id = int(input("Enter the task id : "))
            status = input("Enter new status [completed/in progress/pending] : ")
            update_tasks(task_id=id, status=status)
            print("Status updated successfully")
        elif query =="4":
            tasks = get_task(user_id=user_id)
            for task in tasks:
                print(task)
        elif query =="5":
            break



if __name__== "__main__":
    main()
