# write a python program to creat a class user that store some detail about user and also creat bank class that's stores inforamtion about accont and allow user to check , modify and withdraw balance.

class User():
    def __init__(self,name,gender,age) -> None:
        self.name = name
        self.gender = gender
        self.age = age


    def showdetails(self):
        print(f"Name: {self.name}")
        print(f"gender: {self.gender} ")
        print(f"age: {self.age}")



class bank(User):
    def __init__(self, name, gender, age) -> None:
        super().__init__(name, gender, age)
        self.balacne = 0


    def show_balce(self):
        print(f"your curent balance is {self.balacne}")


    def Add_money(self):
        money = int(input("how many money you want to add in your account: "))
        self.balacne = self.balacne + money
        print("Money transfer Successfully!!")

    def with_draw(self):
        money = int(input("how many money you want to withdraw: "))
        if self.balacne >= money:
            print(f"You take out {money} and your's account balance is {self.balacne}")
        else:
            print(f"Your account balacne is {self.balacne} please slecet the amount in range.")


wahab = User("wahab",34,"male")
Hbl = bank("wahab",34,"male")

Hbl.showdetails()
Hbl.Add_money()
Hbl.show_balce()
Hbl.with_draw()
