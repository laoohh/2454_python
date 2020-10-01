# Please put your first name here (Hans)
class Calculator:
    firstName=""

    def __init__(self, firstName):
        self.firstName=firstName

    def add(self,number1, number2):
        print(self.firstName + ": " + str(number1) + " + " \
              + str(number2) + " = " + str(number1+number2))

    def subtract(self, number1, number2):
        print(self.firstName + ": " + str(number1) + " - " \
              + str(number2) + " = " + str(number1 - number2))


calculator = Calculator("Hans")

calculator.add(3,2)
calculator.add(4,8)
calculator.add(1,7)
calculator.add(4,3)
calculator.subtract(1,4)
calculator.subtract(8,9)