from abc import ABCMeta, abstractmethod

class FileBase(metaclass=ABCMeta):
    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def write_data_to_database(self):
        pass

    def doit():
        print("DO IT!!!")

class FileTypeAAA(FileBase):
    def save_data(self):
        print("saving data")
    def write_data_to_database(self):
        print("saving to db")

f = FileTypeAAA()