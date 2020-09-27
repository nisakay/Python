

#parent class

class User:
    name = "Isaac"
    email = "lionelkay96@gmail.com"
    password = "1234iks"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your Email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#child class emplyee

class Employee(User):
    base_pay = 35.00
    department = "Software Development"
    pin_number = "5852"

#This is the same method in the parent class "User".
#The difference is that instead of using entry_password, I'm using entry_pin

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your Email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorect")

#The following code invokes the methods inside each class for User and Employee

customer =User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
        
