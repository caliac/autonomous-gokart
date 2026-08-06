#skeleton of State object

class State(object):
    def __init__(self):
        #self.state = "IDLE"
        pass

    name = "STATE"

    def __str__(self):
        return self.name

    def initialize(self):
        pass

    def execute(self):
        pass

    def end():
        pass

    def on_event(self, event):
        pass

#note: maybe move this file to autonomous folder