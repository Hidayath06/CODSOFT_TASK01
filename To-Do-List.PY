def show_menu():
    print("\n📝 To-Do List Menu:")
    print("1. View all tasks!")
    print("2. Add a new task!")
    print("3. Mark a task as completed!")
    print("4. Delete a task!")
    print("5. Exit!!")

def view_tasks(tasks):
    if not tasks:
        print("\n📭Oop's Sorry, Your to-do list is empty!")
    else:
        print("\n🔍 Here are your tasks:")
        for i, (task, status) in enumerate(tasks.items(), start=1):
            status_text = "✅ Completed" if status else "⏳ Pending"
            print(f"{i}. {task} [{status_text}]")

def add_task(tasks):
    task = input("\n✍️ Enter the task you want to add: ")
    tasks[task] = False
    print(f"🆕 Task added: '{task}'")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("\n🔖 Enter the task number to mark as completed: "))
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        tasks[task_list[task_number - 1]] = True
        print(f"✅ Task marked as completed: '{task_list[task_number - 1]}'")
    else:
        print("❌ Sorry, Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("\n🗑️ Enter the task number to delete: "))
    task_list = list(tasks.keys())
    if 1 <= task_number <= len(task_list):
        removed_task = task_list[task_number - 1]
        del tasks[removed_task]
        print(f"🗑️ Task deleted: '{removed_task}'")
    else:
        print("❌ Sorry, Invalid task number!")

def todo_list_app():
    tasks = {}
    
    print("📋 Welcome to the To-Do List Application!")
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1/2/3/4/5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\n👋 Have a nice day, Goodbye! Your tasks will be saved for later.")
            break
        else:
            print("❌Sorry, It's Invalid option! Please try again.")
todo_list_app()