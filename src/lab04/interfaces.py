from abc import ABC,abstractmethod
class Reg(ABC):
    @abstractmethod
    def registration():
        pass
class Video(ABC):
    @abstractmethod
    def make_video():
        pass 
class Human (ABC):
    def is_he_humane (self):
        obj = str(self.rep)
        if '-' in obj:
            return False
        return True
    @abstractmethod
    def enter (self):
        pass