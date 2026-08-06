from robot_states import Idle

class RobotStateMachine(object):

    def __init__(self, robot):
        self.robot = robot
        self.state = Idle()
        self.state.enter(robot)

    def on_event(self, event):
        next_state = self.state.on_event(event)

        if next_state.__class__ != self.state.__class__:
            print(f"{self.state} is transitioning to {next_state}")
            self.state.end(self.robot)
            self.state = next_state
            self.state.enter(self.robot)



    def update(self):
        self.state.execute(self.robot)

#note: maybe move this file to autonomous folder