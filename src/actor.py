from .base import Base
from .trigger import TriggerTime

import math

class Actor(Base):
    def __init__(self, scene, name, images, x=0, y=0, face=90, size=100, display=True):
        super().__init__(scene)
        self.name = name
        self.images = images
        self.image = self.images[0]
        self.x = x
        self.y = y
        self.face = face
        self.size = size
        self.display = display
        self.message = ""
        self.is_clone = False
    
    def move(self, step):
        self.x += int(math.sin(self.face / 180 * math.pi)) * step
        self.y += int(math.cos(self.face / 180 * math.pi)) * step
    
    def turn_right(self, angle):
        self.face += angle
    
    def turn_left(self, angle):
        self.face -= angle
    
    def set_location(self, x, y):
        self.x = x
        self.y = y
    
    def set_face(self, face):
        self.face = face
    
    def say(self, message):
        self.message = message

    def clone(self):
        clone = Actor(self.name + "_clone", 
                      self.name,
                      self.images,
                      self.x,
                      self.y,
                      self.face,
                      self.size,
                      self.display)
        clone.triggers = self.triggers
        clone.is_clone = True
        trigger_time = TriggerTime(TriggerTime.Event.Clone)
        if trigger_time in clone.triggers:
            for trigger in clone.triggers[trigger_time]:
                trigger.do()

    def delete_clone(self):
        if self.is_clone:
            self.scene.delete(self)