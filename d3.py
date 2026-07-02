class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20
    def disp(self, x, y):
        z = x + y
        print(z)
d1 = Demo()
print(d1.a)
print(d1.b)
n1 = 100
n2 = 100
d1.disp(n1,n2)