class ConcatStr:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def concatstr_meth(self):
        return self.str1 + self.str2

obj1 = ConcatStr("Sanjeev", "Krishna")
print(obj1.concatstr_meth())
