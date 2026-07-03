# Example: Combining Aggregation and Composition in Python

# -------------------- Composition --------------------
# Heart is a part of Person.
# A Heart cannot exist independently in this example.
class Heart:
    def __init__(self):
        self.status = True
        print("Heart is ready")

    def getHeart(self):
        print("Heart is beating")


# -------------------- Aggregation --------------------
# Car can exist independently of Person.
# Even if Person is deleted, Car object still exists.
class Car:
    def __init__(self, name):
        self.name = name
        print("Car is ready")

    def getCar(self):
        print("Car is running")


# -------------------- Person Class --------------------
class Person:
    def __init__(self, name):
        self.name = name

        # Composition
        # Heart object is created inside Person.
        self.heart = Heart()

        print("Person is ready")

    # Aggregation
    # Person receives an already created Car object.
    def hasPerson(self, car):
        self.c1 = car
        print("Person owns a Car")


# -------------------- Driver Code --------------------

# Create Person object
p = Person("Jayanth")

# Create Car object independently
c = Car("BMW")

# Aggregation
# Pass existing Car object to Person
p.hasPerson(c)

print("\n--- Accessing Objects ---")
print("Person Name :", p.name)
print("Car Name    :", p.c1.name)

# Access Composition object
p.heart.getHeart()

# Access Aggregation object
p.c1.getCar()

# Delete Person object
del p

print("\nAfter deleting Person:")

# The following statements will raise NameError because p is deleted.
# print(p.name)
# print(p.c1.name)
# print(p.heart.status)
# p.heart.getHeart()
# p.c1.getCar()

# Car still exists because of Aggregation
print("Car Name :", c.name)
c.getCar()