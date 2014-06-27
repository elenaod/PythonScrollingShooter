from os import system
from game import *

class Menu:
    def __init__(self, options={}):
        self.options = {"Start a new game" : lambda : self.start(), 
                        "Load last saved game" : lambda : self.load(), 
                        "Exit without saving" : lambda : self.exit(), 
                        "Save and Exit" : lambda : self.save()}
        self._game = Game()

    def present(self):
        #os.system("clear")
        for key in self.options.keys():
            print(key)
        command = input(">:")
        self.options[command]()

    def start(self):
        play(self._game)
        self.present()
    
    def load(self):
        with open("save", 'r') as save_file:
            data = save_file.readline()
            self._game._player.read(data)
            while not data == "---\n":
                data = save_file.readline()
                if not data == "---\n":
                    enemy = Enemy()
                    enemy.read(data)
                    self._game.enemies.append(enemy)
                    self._game._board.place(enemy.x, enemy.y, enemy)
            while not data == "...\n":
                data = save_file.readline()
                if not data == "...\n":
                    bullet = Bullet()
                    bullet.read(data)
                    self._game.bullets.append(bullet)
                    self._game._board.place(bullet.x, bullet.y, bullet)
            while not data == "///\n":
                data = save_file.readline()
                if not data == "///\n":
                    bonus = Bonus()
                    bonus.read(data)
                    self._game.bonuses.append(bonus)
                    self._game._board.place(bonus.x, bonus.y, bonus)
        play(self._game)
         
    def exit(self):
        pass

    def save(self):
        with open("save", 'w') as save_file:
            save_file.write(self._game._player.write() + "\n")
            for enemy in self._game.enemies:
                save_file.write(enemy.write() + "\n")
            save_file.write("---\n")
            for bullet in self._game.bullets:
                save_file.write(bullet.write() + "\n")
            save_file.write("...\n")
            for bonus in self._game.bonuses:
                save_file.write(bonus.write() + "\n")
            save_file.write("///\n")
        self.present()
