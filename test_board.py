import unittest

from board import Board, arrange, collide
from player import Player
from enemy import Enemy
from inanimate import Bullet, Bonus
from misc import MAX_HEALTH

class TestBoard(unittest.TestCase):
    def testPlace(self):
        board = Board(5, 5)
        board.place(2, 3, "string")
        self.assertEqual(board.rows[2][3], "string")

    def testRemove(self):
        board = Board(5, 5)
        board.rows[4][1] = "an object"
        board.remove(4, 1)
        self.assertIsNone(board.rows[4][1])
        board.remove(2, 3)
        self.assertIsNone(board.rows[2][3])

    def testAt(self):
        board = Board(5, 5)
        board.rows[4][1] = "cheese"
        self.assertEqual(board.at(4, 1), "cheese")
        self.assertNotEqual(board.at(4, 0), "cheese")
        self.assertIsNone(board.at(4,2))

    # moving a piece with collision is a single call to
    # collide(...), which is tested separately later
    def testMovePieceWithoutCollision(self):
        board = Board(5, 5)
        player = Player()
        board.rows[2][3] = player
        board.move_piece((2,3), (3, 4))
        self.assertEqual(board.rows[3][4], player)
        self.assertIsNone(board.rows[2][3])

    def testMoveNonExistantPiece(self):
        board = Board(5, 5)
        player = Player()
        board.rows[3][4] = player 
        board.move_piece((1, 3), (3, 4))
        self.assertEqual(board.rows[3][4], player)
        self.assertIsNone(board.rows[1][3])
        board.move_piece((1, 3), (2, 3))
        self.assertIsNone(board.rows[1][3])
        self.assertIsNone(board.rows[2][3])

    def testMovePieseOutsideOfBoard(self):
        board = Board(5, 5)
        player = Player()
        board.rows[1][1] = player
        board.move_piece((1, 1), (-6, 7))
        self.assertEqual(board.rows[1][1], player)

    def testMoveOnDestroyedPiece(self):
        board = Board(5, 5)
        player = Player()
        enemy = Enemy()
        enemy.destroyed = True
        board.rows[1][1] = player
        board.rows[2][2] = enemy 
        board.move_piece((1, 1), (2, 2))
        self.assertEqual(board.rows[2][2], player)
        self.assertIsNone(board.rows[1][1])
        self.assertEqual(player.hits, MAX_HEALTH)

    def testCleanup(self):
        board = Board(5, 5)
        player = Player()
        enemy_one = Enemy()
        enemy_one.destroyed = True
        enemy_two  = Enemy()
        bullet_one = Bullet()
        bullet_one.destroyed = True
        bullet_two = Bullet()
        bullet_two.destroyed = True
        bullet_three = Bullet()
        bonus_one = Bonus()
        bonus_one.destroyed = True
        bonus_two = Bonus()
        board.rows[0][0] = player
        board.rows[1][1] = enemy_one
        board.rows[2][2] = enemy_two
        board.rows[3][3] = bullet_one
        board.rows[4][4] = bullet_two
        board.rows[1][3] = bullet_three
        board.rows[2][0] = bonus_one
        board.rows[3][4] = bonus_two
        board.cleanup()
        self.assertEqual(board.rows[0][0], player)
        self.assertEqual(board.rows[2][2], enemy_two)
        self.assertEqual(board.rows[1][3], bullet_three)
        self.assertEqual(board.rows[3][4], bonus_two)
        self.assertIsNone(board.rows[1][1])
        self.assertIsNone(board.rows[3][3])
        self.assertIsNone(board.rows[4][4])
        self.assertIsNone(board.rows[2][0])

class TestArrange(unittest.TestCase):
    def testArrangePlayerEnemy(self):
        player = Player()
        enemy = Enemy()
        self.assertFalse(arrange(player, enemy))
        self.assertTrue(arrange(enemy, player))

    def testArrangeEnemyBullet(self):
        enemy = Enemy()
        bullet = Bullet()
        self.assertTrue(arrange(bullet, enemy))
        self.assertFalse(arrange(enemy, bullet))

    def testArrangeEnemyBonus(self):
        bonus = Bonus()
        enemy = Enemy()
        self.assertTrue(arrange(bonus, enemy))
        self.assertFalse(arrange(enemy, bonus))

    def testArrangeSame(self):
        player_one = Player()
        player_two = Player()
        enemy_one = Enemy()
        enemy_two = Enemy()
        bullet_one = Enemy()
        bullet_two = Enemy()
        bonus_one = Bonus()
        bonus_two = Bonus()
        self.assertFalse(arrange(player_one, player_two))
        self.assertFalse(arrange(enemy_one, enemy_two))
        self.assertFalse(arrange(bullet_one, bullet_two))
        self.assertFalse(arrange(bonus_one, bonus_two))

    def testArrangeBulletBonus(self):
        bullet = Bullet()
        bonus = Bonus()
        self.assertTrue(arrange(bonus, bullet))
        self.assertFalse(arrange(bullet, bonus))


class TestCollide(unittest.TestCase):
    def testCollidePlayerEnemy(self):
        player = Player()
        enemy = Enemy()
        # just so that we're sure arrange() is called and the pieces
        # properly arranged at the start
        self.assertEqual(collide(player, enemy), "player-enemy")
        self.assertEqual(collide(enemy, player), "player-enemy")

    def testCollidePlayerBullet(self):
        player = Player()
        bullet = Bullet()
        self.assertEqual(collide(player, bullet), "player-bullet")

    def testCollidePlayerBonus(self):
        player = Player()
        bonus = Bonus()
        self.assertEqual(collide(player, bonus), "player-bonus")

    def testCollideSame(self):
        # no test for two players colliding because there can't be two players at once
        # not really sure how two bonuses would collide, but anyways...
        enemy_one = Enemy()
        enemy_two = Enemy()
        self.assertEqual(collide(enemy_one, enemy_two), "enemy-enemy")
        bullet_one = Bullet()
        bullet_two = Bullet()
        self.assertEqual(collide(bullet_one, bullet_two), "bullet-bullet")
        bonus_one = Bonus()
        bonus_two = Bonus()
        self.assertEqual(collide(bonus_one, bonus_two), "bonus-bonus")

    def testCollideEnemyBullet(self):
        enemy = Enemy()
        bullet = Bullet()
        self.assertEqual(collide(enemy, bullet), "enemy-bullet")

    def testCollideEnemyBonus(self):
        enemy = Enemy()
        bonus = Bonus()
        self.assertEqual(collide(enemy, bonus), "enemy-bonus")

    def testCollideBulletBonus(self):
        bonus = Bonus()
        bullet = Bullet()
        self.assertEqual(collide(bonus, bullet), "bullet-bonus")

if __name__ == '__main__':
	unittest.main()
