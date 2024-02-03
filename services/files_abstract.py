from abc import ABC, abstractmethod
class FilesAbstract(ABC) : # use camal case for class name
    def __init__(self, name : str, size : float ,typefap : str, extension : str, users :  list):
        self.name = name
        self.size = size
        self.type = typefap
        self.extension = extension
        self.users = users
from abc import ABCMeta, abstractmethod
class FilesAbstract(metaclass=ABCMeta):
    @abstractmethod
    def read_g(self, extension): # abstract method
        pass
    @abstractmethod
    def modify(self,extension): # abstract method
        pass 
    @abstractmethod
    def copy(self,extension): # abstract method
        pass #TODO
    def remove(self, extension):
        pass #TODO
    def add_user(self, extension):
        pass #TODO
    def delete_user(self, extension):
        pass #TODO