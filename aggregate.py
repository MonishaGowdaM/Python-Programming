class Charger:
    def __init__(self, name):
        self.name = name
        print('Charger is ready')

    def getCharger(self):
        print('Charger is used for charging')


class Mobile:
    def __init__(self, name):
        self.name = name
        print('Mobile is ready')

    def hasMobile(self, x):
        self.c1 = x
        print('Both Charger and Mobile are connected')


m = Mobile('Samsung')

charge = Charger('Samsung Charger')

m.hasMobile(charge)

print(m.name)
print(m.c1.name)

m.c1.getCharger()

del m

print('After deletion:')

# print(m.name)
# print(m.c1.name)

print(charge.name)

charge.getCharger()