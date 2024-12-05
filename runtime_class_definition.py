
class Dog():
    def bark(self):
        print("woof")


def meow(self):
    print("meowwwww!!")

Cat = type("Cat", (), {"meow": lambda self: print("Meowwwww")}) # normally only done at run-time

c = Cat()
c.meow()

class AnimalFactory:
    def make_dog():
        d = Dog()
        return d
    
af = AnimalFactory()
my_dog = af.make_dog()
my_dog.bark()