#code here still needs to be completed, but here is the basic skeleton

from robot_states import RobotState

class RobotStateMachine(object):

    def __init__(self):
        self.state = RobotState.IDLE

    def transition_to(self, new_state):
        self.state = new_state

    def update(self):
        if self.state == RobotState.IDLE:
            self.update_idle()

        elif self.state == RobotState.FOLLOWING_LINE:
            self.update_following_line()

        elif self.state == RobotState.SEARCHING_LINE:
            self.update_searching_line()

    def update_following_line(self):

        pass
        #if obstacle detected,
            #self.transition_to(RobotState.nextstategoeshere)

#note: maybe move this file to autonomous folder