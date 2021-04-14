import threading
from enum import Enum


class TriggerTime:
    class Event(Enum):
        Start = 1
        PressKey = 2
        PressActor = 3
        Background = 4
        Volume = 5
        Message = 6
        Clone = 7

    def __init__(self, event, key=""):
        self.event = event
        self.key = key

    def __hash__(self):
        return hash(str(self.event) + str(self.key))
    
    def __eq__(self, other):
        return self.event == other.event and self.key == other.key

    def __ne__(self, other):
        return self.event != other.event or self.key != other.key


class Trigger:
    def __init__(self, trigger_time):
        self.trigger_time = trigger_time
        self.func = None
        self.thread = None
    
    def then(self, func):
        self.func = func
    
    def isAlive(self):
        if not self.thread:
            return False
        return self.thread.isAlive()

    def do(self, func):
        if self.isAlive():
            return
        self.thread = threading.Thread(target=func)
        self.thread.start()
    
    def wait(self):
        if self.isAlive():
            self.thread.join()
