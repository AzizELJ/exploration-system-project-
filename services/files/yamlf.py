from .files_abstract import FilesAbstract # importation de la classe FilesAbstract
class YamlFile(FilesAbstract) : # inheritance from files_abstract
    def __init__(self, name : str, size : float ,typefap : str, extension : str, users :  list) -> None:
        super().__init__(name, size, typefap, extension, users)
    def read_g(self, extension): # abstract method
        if self.extensionfa == "yaml" :
            fread = open(r"C:\Users\abdo6\OneDrive\Bureau\ExplorationSystemProject\exploration-system-project-\services\files", "r") # besoin de rajouter les files json pour compléter le chemin d'accès
        else :
            pass
    def modify(self,extension): # abstract method
            if self.extensionfa == "yaml" :
                fwrite = open(r"C:\Users\abdo6\OneDrive\Bureau\ExplorationSystemProject\exploration-system-project-\services\files", "w") # besoin de rajouter les files json pour compléter le chemin d'accès
                fwrite.write("write something") # cette ligne peut etre mieux developpée
            else :
                pass
    def copy(self,extension): # abstract method
        pass #TODO
    def remove(self, extension):
        pass #TODO
    def add_user(self, extension):
        pass #TODO
    def delete_user(self, extension):
        pass #TODO