import math

class Actor:
    def __init__(self, scene, name, images, x=0, y=0, face=90, size=100, display=True):
        self.scene = scene
        self.name = name
        self.images = images
        self.image = self.images[0]
        self.x = x
        self.y = y
        self.face = face
        self.size = size
        self.display = display
        self.message = ""
    
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
