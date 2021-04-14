from .trigger import Trigger, TriggerTime

class Background:
    """"""
    def __init__(self, scene, images):
        self.scene = scene
        self.images = images
        self.image = images[0]
        self.index = 0
        self.triggers = []
        self.len = len(images)

    def next_bg(self):
        self.index += 1
        if self.index >= self.len:
            self.index = 0
        self.image = self.images[self.index]
        self.scene.trigger(TriggerTime(TriggerTime.Event.Background, self.index))

    def next_bg_wait(self):
        pass

    def change_bg(self, index):
        self.index = index
        self.image = self.images[self.index]

