import enum
""" 1- add tasks to a list
            2- mark task as complete
            3- view tasks
            4- quit  """
""" In Python, triple-quoted strings are used to create multiline strings.
This syntax allows you to define a string that spans multiple lines without the need for explicit line continuation characters (like \n).
=========================================================================== """
# ================================================================= functions ==============================
tasks=[]
def main():
    massage = """1- add tasks to a list
2- mark task as complete
3- view tasks
4- quit """
        #    massage2="1- add tasks to a list\n"+"2- mark task as complete"+"\n3- view tasks\n"+"4- quit"
    while True:
        print(massage)
        choice=input("Enter your choice bettwen 1-4: ")
        if choice=="1":
            # add tasks to a list
            add_task()
        elif choice=="2":
            # mark task as complete
            mark_task_complete()
        elif choice =="3":
            # view tasks list
            view_tasks()
        elif choice=="4":
            #quit
            break
        else:
            print("you Enter a invalled number :")
def add_task(): 
    # get task form user
    newTask=input("enter task: ")
    note=input("enter a note related to this task: ") 
    # defined task status
    task_info={"task":newTask,"completed":False,"note":note}#dic like a hash map(hash table)
    """ In Python, a dictionary is a built-in data type that allows you to store and retrieve data in a key-value pair format.
      Dictionaries are also known as associative arrays or ==>((hash maps)) in other programming languages.
        The key-value pairs in a dictionary are enclosed in curly braces {}, and the keys and values are separated by colons :. """
    # add task to ttask.ap(newTask)he list of task
    tasks.append(task_info)
    print("the task added successfly")
    
   #1
   #  pass # pass mean i need to defined the function but i am not implements it / just pass it to not take me an erorr(as a return value to stop erorr)
def mark_task_complete():
    # get list of incomplete tasks
    """ incomplete_tasks=[task for task in tasks if task["completed"]==False]]//this a pythonic way eassy in written by it have some exersice OR""" 
    incompleted_tasks=[]
    for task in tasks :
        if (task ["completed"]==False):
            incompleted_tasks.append(task)  
    # check if incompleted task if empty to print this for user
    if len(incompleted_tasks)==0:
        print("no tasks to mark it!!")
        return # to out of function
    # show them to the user
    for i, task in enumerate(incompleted_tasks):
        print(f"{i+1}-{task['task']}")# pythonic way but take sure "''"
    print("-"*30)# make 30 ---
    # get the task form user 
    try :
        task_number=int(input("enter the number of task: "))# i take int number form user
        # mark task as completed
        incompleted_tasks[task_number-1]["completed"]=True # 2D list ==> [{},{},{}]// a=[1,2,3,] if b=a that mean a and b point to same location but b=a.copy that means b takes a copy
        # print message to the user 
    except ValueError:
        print("invalid input , please enter a number!!")
    except IndexError as err:
        print(err)
    print("mark task done")
def view_tasks(tasks):
    #first if there are no task , print message and return function
    if not tasks:
        print("the task list is empty!!!!")
        return
    for i, task in enumerate(tasks):
        if task["completed"]:
            stutas="✔"
            print(f"{i+1}-{task['task']} {stutas}")
        else:
            stutas="❌"
            print(f"{i+1}-{task['task']} {stutas}")  
    print("-"*30)

#print(__name__)#===> if i run this file it will print __main__ // but if i run it by import the module file will print the name of file who run it
if __name__=="__main__":
    main()