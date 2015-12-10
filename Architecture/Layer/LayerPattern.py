class DataLayer:
    def __init__(self):
        self.name = "DataLayer"

    def setlowerlayer(self, lowerlayer):
        self.lowerlayer = lowerlayer

    def sc3(self, param):
        print("Into %s" % self.name)
        self.lowerlayer.sc2(param)
        print("Out of %s" % self.name)

class LogicLayer:
    def __init__(self):
        self.name = "LogicLayer"

    def setLowerLayer(self, lowerlayer):
        self.lowerlayer = lowerlayer

    def sc2(self, param):
        print("Into %s" % self.name)
        self.lowerlayer.sc1(param)
        print("Out of %s" % self.name)

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

    data.setlowerlayer(logic)
    logic.setLowerLayer(ui)

    data.sc3("{name:'Daniel Vega'}")
