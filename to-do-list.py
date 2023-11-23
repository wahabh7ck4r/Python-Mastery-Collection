class To_do_list:

    def __init__(self):
        self.Task = []


    def Add_Task(self):
        user = input("\nEnter the  task you want to Add: ")
        self.Task.append(user)

    def Display_Task(self):
        print(self.Task)

    def Mark_Task(self):
        user = input("\nEnter a task you want to mark: ")
        if user in self.Task:
            with open("Mark_task.txt",'a') as f:
                f.write(f"{user}\n")
                self.Task.remove(user)
        else:
            print("\nThis task is not presetn in the Task please check your list. Thanks!")

    def Delete_Task(self):
        user = input("\nSelect the task you wnat to delet: ")
        try:
            self.Task.remove(user)
        except ValueError :
            print("\nThis task is not presnt in the list please check the list")

    #  you can add more fucntion as your requirment


if __name__ =="__main__":

    ls = To_do_list()

    while True:
        print('''\n  *********   Welcome to To-Do-List  ********** 
            
            1.Add_Task press(a)
            2.Display_task press(d)
            3.Mark_Task press(m)
            4.delte_Task press (dl)
            5.***press(q) to exit the program****
    ''')    
        user = input("choice the given option: ")

        if user == 'a':
            ls.Add_Task()
        elif user == 'd':
            ls.Display_Task()
        elif user == 'm':
            ls.Mark_Task()
        elif user == 'dl':
            ls.Delete_Task()
        elif user == "q":
            break
        else:
            print("please select the valid option")

    print("\n\n*****Thnaks! for using our program*****\n\n")






    