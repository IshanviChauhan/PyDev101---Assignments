print("What do you wanna do:\n1.Create\n2.Edit\n3.List\n4.Delete\n5.Exit\n")
choice=int(input())
taskList = []

def create_task():
    tname=input("Enter task name:")
    taskList.append(tname)
    print("\nTask Created\n")

def display_tasks():
    for i in range(len(taskList)):
        print(f"{i} : {taskList[i]}")

def edit_task():
    tnum = int(input("Which task:"))
    if tnum < len(taskList):
        print(f"\nEditing task : {tnum}\n")
        tchange = input("New name : ")
        taskList[tnum] = tchange
        print("Done editing\n")
    else:
        print("Invalid task number\n")

def delete_task():
    tnum = int(input("Which task: "))
    if tnum < len(taskList):
        del taskList[tnum]
    else:
        print("Invalid task number\n")

while choice!=5:
    if choice == 1:
        create_task()

    elif choice == 2:
        display_tasks()
        edit_task()

    elif choice == 3:
        display_tasks()

    elif choice == 4:
        display_tasks()
        delete_task()

    else:
        print("Enter valid input!")

    print("What do you wanna do:\n1.Create\n2.Edit\n3.List\n4.Delete\n5.Exit\n")
    choice = int(input())

else:
    print("Thanks for using, bye :)")