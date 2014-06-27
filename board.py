import os
from misc import *
from player import Player
from enemy import Enemy
from inanimate import Bullet, Bonus

class Board:
    def __init__(self, size_x=1, size_y=1):
        self.rows = []
        for i in range(0, size_x):
            row = []
            for j in range(0, size_y):
                row.append(None)
            self.rows.append(row)

    # should've made it a collection...
    def place(self, x, y, what):
        if valid(x, y, self):
            self.rows[x][y] = what

    def remove(self, x, y):
        if not outside_of_board(x, y):
            self.rows[x][y] = None
    
    def at(self, x, y):
        if not outside_of_board(x, y):
            return self.rows[x][y]
        else:
            return None

    def move_piece(self, source, target):
        piece_one = self.rows[source[0]][source[1]]
        if piece_one == None:
            pass
        elif not outside_of_board(target[0], target[1]):
            if self.at(target[0], target[1]) == None or self.at(target[0], target[1]).destroyed:
                self.remove(source[0], source[1])
                self.remove(target[0], target[1])
                self.place(target[0], target[1], piece_one)
                piece_one.set_position(target[0], target[1])
            else:
                collide(piece_one, self.at(target[0], target[1]))
        
    # removes any pieces that should be destroyed from the board
    def cleanup(self):
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                if not self.rows[i][j] == None:
                    if self.rows[i][j].destroyed:
                        self.rows[i][j] = None


# a helper function so that we have to check for fewer
# collisions; works because the relation is reflexive
# (if A collides with B then obviously B collided with A)
def arrange(first, second):
    if type(first) == Enemy and type(second) == Player:
        return True
    elif type(first) == Bullet and type(second) != Bonus:
        return True
    elif type(first) == Bonus and type(second) != Bonus:
        return True
    else:
        return False

# the return value is mainly for testing purposes and can
# be removed; however it could still be useful for something
# in-game (statistics for example?!)
def collide(newcomer, other):
    if arrange(newcomer, other):
        third = newcomer
        newcomer = other
        other = third
    if type(newcomer) == Player:
        if type(other) == Enemy:
            newcomer.be_hit(MAX_HEALTH // 2)
            other.be_hit(MAX_HEALTH // 2)
            newcomer.score += 5
            return "player-enemy"
        elif type(other) == Bullet:
            newcomer.be_hit(other.damage)
            other.destroyed = True
            return "player-bullet"
        elif type(other) == Bonus:
            other.destroyed = True
            newcomer.score += other.score
            return "player-bonus"
    elif type(newcomer) == Enemy:
        if type(other) == Enemy:
            newcomer.be_hit(MAX_HEALTH // 2)
            other.be_hit(MAX_HEALTH // 2)
            return "enemy-enemy"
        elif type(other) == Bullet:
            newcomer.be_hit(other.damage)
            if newcomer.destroyed and other._owner == "player":
                other.score += 10
            other.destroyed = True
            return "enemy-bullet"
        elif type(other) == Bonus:
            other.destroyed = True
            return "enemy-bonus"
    elif type(newcomer) == Bullet:
        if type(other) == Bullet:
            newcomer.destroyed = True
            other.destroyed = True
            return "bullet-bullet"
        elif type(other) == Bonus:
            other.destroyed = True
            return "bullet-bonus"
    elif type(newcomer) == Bonus:
        if type(other) == Bonus:
            newcomer.destroyed = True
            other.destroyed = True
            return "bonus-bonus"
