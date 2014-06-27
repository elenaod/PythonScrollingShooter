from random import randint
from misc import *
from board import *
from misc import *
from player import *
from enemy import *
from inanimate import *

def show_console(game):
    #os.system("clear")
    for row in game._board.rows:
        for column in row:
            if type(column) == Enemy:
                print("X", end=" ")
            elif type(column) == Player:
                print("@", end=" ")
            elif type(column) == Bullet:
                print(".", end=" ")
            elif type(column) == Bonus:
                print("o", end=" ")
            elif column is None:
                print("_", end=" ")
        print()


class Game:
    def __init__(self):
        self._board = Board(SIZE, SIZE) 
        self._player = Player(SIZE - 1, SIZE//2 - 1)
        self._board.place(self._player.x, self._player.y, self._player)
        self.running = True
        self.enemies = []
        self.bullets = []
        self.commands = {"move_player_left" : lambda : self._move_player((0,-1)), 
                         "move_player_right" : lambda : self._move_player((0,1)),
                         "move_player_up" : lambda : self._move_player((-1,0)),
                         "move_player_down" : lambda : self._move_player((1,0)),
                         "player_shoot" : lambda : self._add_bullet(),
                         "game_stop" : lambda : self._stop()}

    def _move_player(self, dirs):
        source = (self._player.x, self._player.y)
        target = (self._player.x + dirs[0], self._player.y + dirs[1])
        self._board.move_piece(source, target)

    def _add_bullet(self):
        new_bullet = self._player.shoot()
        self._board.place(new_bullet.x, new_bullet.y, new_bullet)
        self.bullets.append(new_bullet)

    def _process_command(self, command):
        self.commands[command]()

    def _stop(self):
        self.running = False
    
    def _remove(self, what):
        if not outside_of_board(what.x, what.y):
            self._board.remove(what.x, what.y)
        if type(what) == Bullet:
            self.bullets.remove(what)
        elif type(what) == Enemy:
            self.enemies.remove(what)

    def _move_enemies(self):
        for enemy in self.enemies:
            source = (enemy.x, enemy.y)
            target = (enemy.x + enemy.dirs[0], enemy.y + enemy.dirs[1])
            self._board.move_piece(source, target)
        for enemy in self.enemies:
            if enemy.destroyed:
                self.enemies.remove(enemy)
                chance = randint(0,10)
                if chance <= 2 and not outside_of_board(enemy.x + 1, enemy.y):
                    bonus = Bonus(enemy.x, enemy.y, self._player.score // 10)
                    self._board.place(enemy.x, enemy.y, bonus)
        
    def _move_bullets(self):
        for bullet in self.bullets:
            source = (bullet.x, bullet.y)
            target = (bullet.x + bullet.dirs[0], bullet.y + bullet.dirs[1])
            self._board.move_piece(source, target)
        for bullet in self.bullets:
            if bullet.destroyed:
                self._player.score += bullet.score
                self.bullets.remove(bullet)

    def move(self):
        self._move_enemies()
        self._move_bullets()                        
                        
    def spawn_enemy(self):
        y = randint(0, SIZE - 1)
        while self._board.rows[0][y] != None:
            y = randint(0, SIZE - 1)
        new_enemy = Enemy(0, y, wave=self._player.score // 10 + 1)
        self.enemies.append(new_enemy)
        self._board.place(new_enemy.x, new_enemy.y, new_enemy)  
    
    def handle_timers(self):
        self._player.time()
        for enemy in self.enemies:
            enemy.time()
        
def play(game):
    while game.running:
        show_console(game)
        print("SCORE: ", game._player.score, "HITS: ", game._player.hits)
        game.spawn_enemy()
        command = get_command_console()
        game._process_command(command)            
        game.move()
        if game._player.destroyed:
            print("GAME OVER!")
            game._running = False
        game.handle_timers()
