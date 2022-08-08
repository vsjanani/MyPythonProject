from dummy import ConcatStr

class ChildConcatStr (ConcatStr):

    str3 = "janani"
    #def __init__(self):
     #   ConcatStr.__init__(self, "Darshini", "Dinesh")

    def concatstr_child_meth(self):
        return self.concatstr_meth() + self.str3


obj2 = ChildConcatStr("Darshini", "Dinesh")
print(obj2.concatstr_meth())
print(obj2.concatstr_child_meth())