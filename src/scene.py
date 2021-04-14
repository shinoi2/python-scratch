from .actor import Actor
from .background import Background

class Scene:
    def __init__(self):
        self.objects = []
    
    def trigger(self, trigger_time):
        for obj in self.objects:
            if trigger_time in obj.triggers:
                for trigger in obj.triggers[trigger_time]:
                    trigger.do()
    
    def delete(self, obj):
        self.objects.remove(obj)
    
    def display(self):
        for obj in self.objects:
            if isinstance(obj, Actor):
                Display.show(obj.image, obj.x, obj.y, obj.size)
            if isinstance(obj, Background):
                Display.show(obj.image, 0, 0, 100)
                
actor = Actor()

def my_func():
    actor.move(10)
    actor.message("123")

actor.when(trigger_time).then(my_func)

