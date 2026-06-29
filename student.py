class Student():
    def __init__(self):
        self.name = 'Monisha'
        self.age = 23
        self.usn = '1DB22CS406'
        self.gender = 'Female'
        self.cgpa = 8.96
    def working(self):
        print('student is working')
    def studying(self):
        print('student is studying')
    def walking(self):
        print('student is walking')
s1 = Student()
s1.working()
s1.studying()
s1.walking()
print(s1.name)
print(s1.age)
print(s1.usn)
print(s1.gender)
print(s1.cgpa)