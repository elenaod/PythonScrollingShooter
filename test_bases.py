import unittest

from misc import TIMER, MAX_HEALTH
from bases import *

class TestFlyingObject(unittest.TestCase):
    def testPosition(self):
        flying = FlyingObject()
        flying.set_position(5, 4)
        self.assertEqual(flying.x, 5)
        self.assertEqual(flying.y, 4)

    def testTimeWithoutReset(self):
        flying = FlyingObject()
        flying.timer = 3
        flying.time()
        self.assertEqual(flying.timer, 2)

    def testTimeReset(self):
        flying = FlyingObject()
        flying.timer = 1
        flying.time()
        self.assertEqual(flying.timer, TIMER)

    def testRead(self):
        flying = FlyingObject()
        flying.read("10 12 5 False")
        self.assertEqual(flying.x, 10)
        self.assertEqual(flying.y, 12)
        self.assertEqual(flying.timer, 5)
        self.assertFalse(flying.destroyed)

    def testWrite(self):
        flying = FlyingObject(7, 3)
        test_write = flying.write()
        self.assertEqual(test_write, "7 3 5 False")

class TestAnimateObject(unittest.TestCase):
    def testBeHitAndDestroyed(self):
        animated = AnimateObject()
        animated.be_hit(2 * MAX_HEALTH)
        self.assertTrue(animated.destroyed)
    
    def testBeWounded(self):
        animated = AnimateObject()
        animated.be_hit(1)
        self.assertEqual(animated.hits, MAX_HEALTH - 1)
        self.assertFalse(animated.destroyed)

    def testRefreshingWhenHealthy(self):
        animated = AnimateObject()
        animated._refresh()
        self.assertEqual(animated.hits, MAX_HEALTH)

    def testRefreshingWhenHurt(self):
        animated = AnimateObject()
        animated.hits = 1
        animated._refresh()
        self.assertEqual(animated.hits, 2)
        
    def testRead(self):
        animated = AnimateObject()
        animated.read("10 12 5 False 20 2")
        self.assertEqual(animated.x, 10)
        self.assertEqual(animated.y, 12)
        self.assertEqual(animated.timer, 5)
        self.assertFalse(animated.destroyed)
        self.assertEqual(animated.hits, 20)
        self.assertEqual(animated.regenerate, 2)

    def testWrite(self):
        animated = AnimateObject(7, 3, 15, 3)
        test_write = animated.write()
        self.assertEqual(test_write, "7 3 5 False 15 3")

if __name__ == '__main__':
    unittest.main()
