from enum import Enum

size = 10
duration = 10

class direction(Enum):
    left = -1
    right = 1

def opposite(name):
    if name == "invincible":
        return "ninja on board"
    elif name == "weapon boost":
        return "weapon broken"
    elif name == "weapon broken":
        return "weapon boost"
    elif name == "ninja on board":
        return "invincible"
    else
        return None


class Bullet:
    def __init__(self, pos_x, pos_y, attack, owner):
        self.row = pos_x
        self.column = pos_y
        self.damage = attack
        self.owner = owner

    def move(self):
        if owner == "player":
            self.row += 1
        else:
            self.row -= 1


class Player:
    def __init__(self):
        self.health = 100
        self._position = 2
        self.score = 0
        self._wave = 0
        self._buffs = {"invincible" : 0, "weapon boost" : 0, "weapon broken" : 0, "ninja on board" : 0}
    
    def move(self, direction):
        if self.position + direction >= 0 and self.position + direction < size
            self.positions += direction

    def catch_boost(self, buff):
        self._buffs[buff] += duration - self._buffs[opposite(buff)]
        self._buffs[opposite(buff)] = 0

    def shoot(self):
        return Bullet(2, self._position, (_buffs["weapon boost"] + _buffs["weapon broken"] + 1) * 10)

    def collide(self, other):
        if other is Bullet:
            health -= other.damage
        elif other is Enemy:
            health = 0

class Enemy:
    def __init__(self, wave, column):
        self.health = wave * size
        self.row = size
        self.column = column
        self.attack = False

    def move(self, direction):
        if not self.attack:
            self.row += 1
        else:
            self.row += direction

    def shoot(self):
	    if self.attack:
	        return Bullet(self.row - 1, self.column, 10)
        else:
            return None
