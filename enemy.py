from bases import *

class Enemy(AnimateObject):
    def __init__(self, x=0, y=0, hits=MAX_HEALTH, timer=TIMER, ranged=False, wave=1):
        super(Enemy, self).__init__(x, y, hits, timer)
        self.hits = self.hits * wave
        self.shooting = ranged
        self.dirs = (1, 0)
        
    def read(self, data):
        super(Enemy, self).read(data)
        values = data.split(" ")
        self.shooting = values[6] == 'True'
        self.dirs = (int(values[7]), int(values[8]))

    def write(self):
        data = super(Enemy, self).write()
        data += " " + str(self.shooting)
        data += " " + str(self.dirs[0]) + " " + str(self.dirs[1])
        return data

    def caclulate_dirs(self):
        pass
