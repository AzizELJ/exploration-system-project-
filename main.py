######### CODE SOURCE FOR CHECKING THE CURRENT WORKSPACE DIRECTORY #########

# import os
# # print(os.getcwd())
# # print(os.path.abspath('..'))
# os.chdir(r"C:\Users\abdo6\OneDrive\Bureau\ExplorationSystemProject")
# print(os.getcwd())

######### END CODE SOURCE FOR CHECKING THE CURRENT WORKSPACE DIRECTORY #########

from abc import ABC, abstractmethod
class FilesAbstract(ABC) : # use camal case for class name
    def __init__(self, name : str, size : float ,typefap : str, extension : str, users :  list):
        self.namefa = name
        self.sizefa = size
        self.typefa = typefap
        self.extensionfa = extension
        self.usersfa = users
    def read_g(self, fread, extensionfa): # abstract method
        if self.extensionfa == "yaml" : # use type and path as attributes
            fread = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\yamlmodule", "r") # besoin de rajouter les files yaml pour compléter le chemin d'accès 
        elif self.extensionfa == "json" :
            fread = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\jsonmodule", "r") # besoin de rajouter les files json pour compléter le chemin d'accès
        elif self.extensionfa == "txt" :
            fread = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\txtmodule", "r") # besoin de rajouter les files txt pour compléter le chemin d'accès
        else :
            pass
    @abstractmethod
    def modify(self, fwrite, extensionfa):
        if self.extensionfa == "yaml" :
            fwrite = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\yamlmodule", "w") # besoin de rajouter les files yaml pour compléter le chemin d'accès 
            fwrite.write("write something") # cette ligne peut etre mieux developpé
        elif self.extensionfa == "json" :
            fwrite = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\jsonmodule", "w") # besoin de rajouter les files json pour compléter le chemin d'accès
            fwrite.write("write something") # cette ligne peut etre mieux developpée
        elif self.extensionfa == "txt" :
            fwrite = open(r"C:\Users\abdo6\OneDrive\Bureau\Python courses\Systeme d'exploration project\files package\txtmodule", "w") # besoin de rajouter les files txt pour compléter le chemin d'accès
            fwrite.write("write something") # cette ligne peut etre mieux developpée
        else :
            pass
    def copy(self): # abstract method
        pass #TODO
    def remove(self):
        pass #TODO
    def add_user(self):
        pass #TODO
    def delete_user(self):
        pass #TODO