class Meta(type):

    def __prepare__(class_name, bases):
        """
        "Prepare" the new class. Here you can update the base classes.

        :param name: Name of new class as a string
        :param bases: Tuple of base classes
        :return: Dictionary that initializes the namespace for the new class (must be a dict)
        """
        print(f"in metaclass (class={class_name}) __prepare__()", end=' ==> ')
        print(f"params: name={class_name}, bases={bases}")
        return {'animal': 'wombat', 'id': 100}

    def __new__(metatype, name, bases, attrs):
        """
        Create the new class. Called after __prepare__(). Note this is only called when classes

        :param metatype: The metaclass itself
        :param name: The name of the class being created
        :param bases: bases of class being created (may be empty)
        :param attrs: Initial attributes of the class being created
        :return:
        """
        print(f"in metaclass (class={name}) __new__()", end=' ==> ')
        print(f"params: type={metatype} name={name} bases={bases} attrs={attrs}")
        return super().__new__(metatype, name, bases, attrs)

    def __init__(cls, *args):
        """

        :param cls: The class being created (compare with 'self' in normal class)
        :param args: Any arguments to the class
        """
        print(f"in metaclass (class={cls.__name__}) __init__()", end=' ==> ')
        print(f"params: cls={cls}, args={args}")

        super().__init__(cls)

    def __call__(self, *args, **kwargs):
        """
        Function called when the metaclass is called, as in NewClass = Meta(...)

        :param args:
        :param args:
        :param kwargs:
        :return:
        """
        print(f"in metaclass (class={self.__name__})__call__()")


class MyBase():
    pass

print('=' * 60)

class A(MyBase, metaclass=Meta):
    id = 5

    def __init__(self):
        print("In class A __init__()")

print('=' * 60)

class B(MyBase, metaclass=Meta):
    animal = 'wombat'

    def __init__(self):
        print("In class B __init__()")


print('-' * 60)
m1 = A()
print('-' * 60)
m2 = B()
print('-' * 60)
m3 = A()
print('-' * 60)
m4 = B()
print('-' * 60)
print(f"animal: {A.animal} id: {B.id}")
