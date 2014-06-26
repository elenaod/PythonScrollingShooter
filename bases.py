"""
Defines base classes for all possible objects in the scrolling shooter.
"""

from misc import TIMER, MAX_HEALTH

class FlyingObject:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.timer = TIMER
        self.destroyed = False

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def _refresh(self):
        pass

    def time(self):
        self.timer -= 1
        if self.timer <= 0:
            self._refresh()            
            self.timer = TIMER

    def read(self, data):
        values = data.split(" ")
        self.x = int(values[0])
        self.y = int(values[1])
        self.timer = int(values[2])
        self.destroyed = values[3] == True

    def write(self):
        data = str()
        data += str(self.x) + " "
        data += str(self.y) + " "
        data += str(self.timer) + " "
        data += str(self.destroyed)
        return data


class AnimateObject(FlyingObject):
    def __init__(self, x=0, y=0, hits=MAX_HEALTH, regenerate=1):
        super(AnimateObject, self).__init__(x, y)
        self.hits = hits
        self.regenerate = regenerate

    def be_hit(self, damage):
        self.hits -= damage
        if self.hits <= 0:
            self.destroyed = True

    def _refresh(self):
        self.hits += self.regenerate
        if self.hits >= MAX_HEALTH:
            self.hits = MAX_HEALTH

    def read(self, data):
        super(AnimateObject, self).read(data)
        values = data.split(" ")
        self.hits = int(values[4])
        self.regenerate = int(values[5])

    def write(self):
        data = super(AnimateObject, self).write()
        data += " " + str(self.hits)
        data += " " + str(self.regenerate)
        return data        
