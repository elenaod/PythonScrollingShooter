import unittest

from inanimate import Bullet, Bonus

class TestBullet(unittest.TestCase):
    def testRead(self):
        bullet = Bullet()
        bullet.read("3 5 12 False player 2 10 -3 4")
        self.assertEqual(bullet.x, 3)
        self.assertEqual(bullet.y, 5)
        self.assertEqual(bullet.timer, 12)
        self.assertFalse(bullet.destroyed)
        self.assertEqual(bullet._owner, "player")
        self.assertEqual(bullet.damage, 2)
        self.assertEqual(bullet.score, 10)
        self.assertEqual(bullet.dirs, (-3,4))

    def testWriteWithDirsOverwrite(self):
        bullet = Bullet(8, 6, "player", 1, (3, 3))
        test_write = bullet.write()
        self.assertEqual(test_write, "8 6 5 False player 1 0 -1 0")

    def testWriteWithoutDirsOverwrite(self):
        bullet = Bullet(8, 6, "nobody", 1, (3, 3))
        test_write = bullet.write()
        self.assertEqual(test_write, "8 6 5 False nobody 1 0 3 3")

class TestBonus(unittest.TestCase):
    def testRefresh(self):
        bonus = Bonus()
        bonus._refresh()
        self.assertTrue(bonus.destroyed)
    
    def testRead(self):
        bonus = Bonus()
        bonus.read("9 2 3 False 15")
        self.assertEqual(bonus.x, 9)
        self.assertEqual(bonus.y, 2)
        self.assertEqual(bonus.timer, 3)
        self.assertFalse(bonus.destroyed)
        self.assertEqual(bonus.score, 15)
        
    def testWrite(self):
        bonus = Bonus(9, 4, 10, 3)
        test_write = bonus.write()
        self.assertEqual(test_write, "9 4 5 False 30")


if __name__ == '__main__':
    unittest.main()
