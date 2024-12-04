
class Dog():
    def bark(self):
        print("woof")


def meow(self):
    print("meowwwww!!")

Cat = type("Cat", (), {"meow": lambda self: print("Meowwwww")})

c = Cat()
c.meow()