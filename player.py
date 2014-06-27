from bases import *
from inanimate import Bullet

class Player(AnimateObject):
    def __init__(self, x=0, y=0, hits=MAX_HEALTH, timer=TIMER, damage=1, score=0):
        super(Player, self).__init__(x, y, hits, timer)
        self.damage = damage
        self.score = score
                
    def shoot(self):
        if self.x - 1 >= 0:
            return Bullet(self.x - 1, self.y, "player", self.damage)

    def read(self, data):
        super(Player, self).read(data)
        values = data.split(" ")
        self.score = int(values[6])
        self.damage = int(values[7])

    def write(self):
        data = super(Player, self).write()
        data += " " + str(self.damage)
        data += " " + str(self.score)
        return data
