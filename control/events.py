#enum of all possible robot events

from enum import Enum

class Event(Enum):
    OBSTACLE = 1
    NO_OBSTACLE = 2
    DRIVE = 3
    LINE_LOST = 4
    LINE_FOUND = 5
    ESTOP = 6
    RESET = 7

#note: maybe move this file to autonomous folder