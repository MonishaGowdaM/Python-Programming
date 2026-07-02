class Farmer:
    r = 2.5
    def __init__(self,p,t):
        self.p = p
        self.t = t
    def disp(self):
        SI = (self.p * self.t * Farmer.r)/100
        print(SI)
f1 = Farmer(100000,2)
f2 = Farmer(200000,2)
f3 = Farmer(300000,5)
f1.disp()
f2.disp()
f3.disp()