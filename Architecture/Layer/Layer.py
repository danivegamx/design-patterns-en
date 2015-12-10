"""
 Design Patterns v1

 Architecture -> Layer
 Python
 Daniel Vega Ceja, 2015
"""
# The layers, are representations of the server-client development architecture

# Data layer or Database.
class DataLayer:
    def __init__(self):
        self.name = "DataLayer"

    def setlowerlayer(self, lowerlayer):
        self.lowerlayer = lowerlayer

    def sc3(self, param):
        print("Into %s" % self.name)
        self.lowerlayer.sc2(param)
        print("Out of %s" % self.name)

# Backend layer.
class LogicLayer:
    def __init__(self):
        self.name = "LogicLayer"

    def setLowerLayer(self, lowerlayer):
        self.lowerlayer = lowerlayer

    def sc2(self, param):
        print("Into %s" % self.name)
        self.lowerlayer.sc1(param)
        print("Out of %s" % self.name)

# Frontend layer.
class PresentationLayer:
    def __init__(self):
        self.name = "PresentationLayer"

    def setLowerLayer(self, lowerlayer):
        self.lowerlayer = lowerlayer

    def sc1(self, param):
        print("Into %s" % self.name)
        print("Presentation service (S1) -> %s" % param)
        print("Out of %s" % self.name)

if __name__ == "__main__":
    ui = PresentationLayer()
    logic = LogicLayer()
    data = DataLayer()

    # Identifying lower layers in the architecture.
    data.setlowerlayer(logic)
    logic.setLowerLayer(ui)

    # Retrieving a JSON from the database.
    data.sc3("{name:'Daniel Vega'}")
