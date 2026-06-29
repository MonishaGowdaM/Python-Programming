class Fan:
    def __init__(self):
        self.brand = 'Bajaj'
        self.color = 'Black'
        self.cost = 5000
        self.no_of_blades = 3
    def switch_on(self):
        print('Fan is switched on')
    def switch_off(self):
        print('Fan is switched off')
    def rotate(self):
        print('Fan is rotating')
f1 = Fan()
f1.switch_on()
f1.switch_off()
f1.rotate()
print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.no_of_blades)