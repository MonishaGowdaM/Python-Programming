class Fan:
    def __init__(self):
        self.brand = 'Bajaj'
        self.color = 'Ivory'
        self.price = 2500
        self.no_of_blades = 3
        print(self)
f1 = Fan()
print(f1)
f2 = f1
print(f2)
print(id(f1))
print(id(f2))
print(f1 is f2)