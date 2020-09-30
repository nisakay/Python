from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
#This function is to pass in an argument
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
    #here we define how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit'.format(amount))

obj = DebitCardPayment()
obj.paySlip("500")
obj.payment("500")
