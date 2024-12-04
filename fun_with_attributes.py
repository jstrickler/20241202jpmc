cities = []
cities.append("Columbus")

print(dir(cities))

a = getattr(cities, 'append')
print(f"{a = }")
a("Pittsburgh")
print(f"{cities = }")

if hasattr(cities, "write"):
    print("Has a write() method")
else:
    print("Does not have a write() method")

# getattr() hasattr() setattr() delattr()

class Dog:
    pass

def speak(self):
    print("Woof! Woof!")

d = Dog()

setattr(Dog, "bark", speak)

d.bark()

# delattr(Dog, "bark")

# d.bark()

def spam():
    pass

setattr(spam, "color", "blue")
print(spam.color)

