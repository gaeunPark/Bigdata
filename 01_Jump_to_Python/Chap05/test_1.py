class Calculator:
    def __init__(self, args):
        self.args = args
        self.result = 0

    def sum(self):
        for i in self.args:
            self.result += i
        return  self.result

    def avg(self):
        self.result = self.result/len(self.args)
        return self.result



cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

