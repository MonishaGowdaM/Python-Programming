class Radio:
    def turnon(self, x):
        if x == 1:
            print("Radio ON")
        else:
            print("Radio OFF")
class Car:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.radio = Radio() #Delegation
c = Car(60, 120)
print(c.min)
print(c.max)
c.radio.turnon(1)
c.radio.turnon(2)