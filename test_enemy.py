import unittest

from enemy import Enemy

class TestEnemy(unittest.TestCase):
    def testRead(self):
        enemy = Enemy()
        enemy.read("10 12 5 False 20 2 True 3 4")
        self.assertEqual(enemy.x, 10)
        self.assertEqual(enemy.y, 12)
        self.assertEqual(enemy.timer, 5)
        self.assertFalse(enemy.destroyed)
        self.assertEqual(enemy.hits, 20)
        self.assertEqual(enemy.regenerate, 2)
        self.assertEqual(enemy.shooting, True)
        self.assertEqual(enemy.dirs, (3,4))

    def testWrite(self):
        enemy = Enemy(7, 3, 15, 3, True, 2)
        enemy.dirs = (-1, 2)
        test_write = enemy.write()
        self.assertEqual(test_write, "7 3 5 False 30 3 True -1 2")

if __name__ == '__main__':
    unittest.main()
