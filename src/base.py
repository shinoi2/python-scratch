from .trigger import Trigger, TriggerTime
import time

class Base:
    def __init__(self, scene):
        self.scene = scene
        self.triggers = {}

    def when(self, trigger_time):
        trigger = Trigger(trigger_time)
        if trigger_time not in self.triggers:
            self.triggers[trigger_time] = [trigger]
        else:
            self.triggers[trigger_time].append(trigger)
        return trigger
    
    def boradcast(self, message):
        self.scene.trigger(TriggerTime(TriggerTime.Event.Message, message))
    
    def boradcast_wait(self, message):
        self.scene.wait(TriggerTime(TriggerTime.Event.Message, message))
    
    def wait(self, seconds):
        time.sleep(seconds)

