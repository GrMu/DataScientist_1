from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):        # empty definition
        pass
    def calc_area(self):
        pass

    def noofsides(self):
        print("I have 4 sides.")
    def calc_area(self,b,h):
        return (b*h)
