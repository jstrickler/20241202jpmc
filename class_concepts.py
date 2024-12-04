cities = list()

cities.append("Durham")
cities.append("Buenos Aires")
print("cities[0]")
flags = [True] * 10
print(flags)

x = 5   #  x = int(5)       int x = new int(5);

class Animal:
    def move(self):
        print("moving")

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d = Dog()
d.move()
d.bark()

d = Dog("Frank", "Border Collie")
