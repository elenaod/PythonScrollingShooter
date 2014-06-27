import unittest

from player import Player
from inanimate import Bullet

class TestPlayer(unittest.TestCase):
    def compare_bullets(self, first, second):
        return first.x == second.x and first.y == second.y and first.destroyed == second.destroyed and first.damage == second.damage

    def testShootInsideBoard(self):
        player = Player(3, 4)
        test_bullet = Bullet(2, 4, "player", 1)
        bullet = player.shoot()
        self.assertTrue(self.compare_bullets(bullet, test_bullet))

    def testShootBarelyInsideBoard(self):
        player = Player(1, 8)
        test_bullet = Bullet(0, 8, "player", 1)
        bullet = player.shoot()
        self.assertTrue(self.compare_bullets(bullet, test_bullet))

    def testShootOutsideBoard(self):
        player = Player(0, 5)
        self.assertIsNone(player.shoot())

    def testRead(self):
        player = Player()
        player.read("10 12 5 False 20 2 100 2")
        self.assertEqual(player.x, 10)
        self.assertEqual(player.y, 12)
        self.assertEqual(player.timer, 5)
        self.assertFalse(player.destroyed)
        self.assertEqual(player.hits, 20)
        self.assertEqual(player.regenerate, 2)
        self.assertEqual(player.score, 100)
        self.assertEqual(player.damage, 2)

    def testWrite(self):
        player = Player(7, 3, 15, 3, 4, 235)
        test_write = player.write()
        self.assertEqual(test_write, "7 3 5 False 15 3 4 235")

if __name__ == '__main__':
    unittest.main()
