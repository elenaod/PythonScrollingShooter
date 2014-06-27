from bases import FlyingObject

class Bullet(FlyingObject):
    def __init__(self, x=0, y=0, owner="player", damage=3, dirs=(0,0)):
        super(Bullet, self).__init__(x, y)
        self._owner = owner
        self.damage = damage
        self.score = 0
        self.dirs = dirs
        if owner == "player":
            self.dirs = (-1, 0)
        elif owner == "enemy":
            self.dirs = (1, 0)

    def read(self, data):
        super(Bullet, self).read(data)
        values = data.split(" ")
        self._owner = values[4]
        self.damage = int(values[5])
        self.score = int(values[6])
        self.dirs = (int(values[7]), int(values[8]))
    
    def write(self):
        data = super(Bullet, self).write()
        data += " " + str(self._owner)
        data += " " + str(self.damage)
        data += " " + str(self.score)
        data += " " + str(self.dirs[0]) + " " + str(self.dirs[1])
        return data

class Bonus(FlyingObject):
    def __init__(self, x=0, y=0, score=20, wave=1):
        super(Bonus, self).__init__(x, y)
        self.score = score * wave
    
    def _refresh(self):
        self.destroyed = True

    def read(self, data):
        super(Bonus, self).read(data)
        values = data.split(" ")
        self.score = int(values[4])

    def write(self):
        data = super(Bonus, self).write()
        data += " " + str(self.score)
        return data
