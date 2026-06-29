#each individual state

from state import State
from events import Event

class Idle(State):

    name = "IDLE"

    def enter(self):
        pass
        #stop all motors, keep robot idle

    def on_event(self, event):
        if event == Event.ESTOP:
            return EStopped()
        if event == Event.DRIVE:
            return SearchingLine()    

        return self

class Braking(State):

    name = "BRAKING"

    def initialize(self):
        pass

    def on_event(self, event):
        if event == Event.ESTOP:
            return EStopped()
        if event == Event.NO_OBSTACLE:
            return SearchingLine()

        return self

class SearchingLine(State):

    name = "SEARCHING_LINE"

    def initialize(self):
        pass

    def execute(self):
        pass
        #repeated loop of xxx

    def on_event(self, event):
        if event == Event.ESTOP:
            return EStopped()
        if event == Event.LINE_FOUND:
            return FollowingLine()
        if event == Event.OBSTACLE:
            return Braking()

        return self

class FollowingLine(State):

    name = "FOLLOWING_LINE"

    def initialize(self):
        pass

    def execute(self):
        pass
        #repeated loop of xxx

    def on_event(self, event):
        if event == Event.ESTOP:
            return EStopped()
        if event == Event.OBSTACLE:
            return Braking()
        if event == Event.LINE_LOST:
            return SearchingLine()

        return self

class EStopped(State):

    name = "E_STOPPED"

    def initialize(self):
        pass
        #stop everything

    def on_event(self, event):
        if event == Event.RESET:
            return Idle()

        return self