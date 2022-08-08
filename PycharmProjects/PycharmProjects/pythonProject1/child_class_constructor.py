from parent_class_constructor import AddThreeNum


class AddFourNum(AddThreeNum):
    num4 = 40

    def __init__(self):
        AddThreeNum.__init__(self, 50, 60)

    def add_four(self):
        print("parent class check in child class:", self.add_three())
        return self.num4 + self.num1 + self.add_three()


AddObj2 = AddFourNum(50, 600)
print(AddObj2.add_four())
