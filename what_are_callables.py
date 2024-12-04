

# x()

# function
def spam():
    pass

# class
class Ham():
    # method
    def toast(self):
        pass
    def __call__(self):
        print("wahoooooo")

spam()     # function
h = Ham()  # class
h.toast()  # method
h() # callable "class", really callable instance

print(dir(spam))
