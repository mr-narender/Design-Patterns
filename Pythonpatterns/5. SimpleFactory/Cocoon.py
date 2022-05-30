
class Butterfly():
    def addSub(self,x,y): pass

class TrigButterfly(Butterfly):
    def addSub(self,x,y):pass

class AddButterfly(Butterfly):
    def addSub(self, x, y):pass

class Cocoon():
    def getButterfly(self, y:float):
        return TrigButterfly(y) if y !=0 else AddButterfly(y)