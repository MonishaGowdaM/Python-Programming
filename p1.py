class Hero:
    def __init__(self):
        self.name = 'Darshan'
        self.age = 47
        self.height = 6.3
        self.mob = 9876543210
    def act(self):
        print('Hero is dancing')
    def dance(self):
        print('Hero is dancing')
h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.mob)
h1.mob = 1234567890
h1.age = 48
h1.no_of_movies = 50
h1.no_of_hits = 30
h2 = h1
h3 = h2
print(h3.name)
print(h2.age)
print(h1.height)
print(h2.mob)
print(h3.no_of_movies)
print(h2.no_of_hits)
h3.act()
h1.dance()