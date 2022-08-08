class AddThreeNum:
    num1 = 10

    def __init__(self, num2, num3):
        self.num2 = num2
        self.num3 = num3

    def add_three(self):
        return self.num1 + self.num2 + self.num3


AddObj1 = AddThreeNum(20, 30)
print(AddObj1.add_three())
print("hello")
#print(Sum_Output)


