class Demo:
    def __init__(self):
        self.a = 10
        self.b = 20
    def disp(self):
        print(self.a)
        print(self.b)
        self.c = 30
        self.d = 40
d1 = Demo()
print(d1.a)
print(d1.b)
d1.disp()
d1.e = 50
d1.f = 60
print(d1.c)
print(d1.d)
print(d1.e)
print(d1.f)