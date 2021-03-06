import unittest

from misc import *
from board import Board

class TestMisc(unittest.TestCase):
    def testOutsideOfBoardBelow(self):
        self.assertTrue(outside_of_board(SIZE + 5, 4))
    
    def testOutsideOfBoardAbove(self):
        self.assertTrue(outside_of_board(-5, 2))

    def testOutsideOfBoardToTheRight(self):
        self.assertTrue(outside_of_board(7, SIZE))

    def testOutsideOfBoardToTheLeft(self):
        self.assertTrue(outside_of_board(9, -2))

    def testCompletelyOutsideOfBoard(self):
        self.assertTrue(outside_of_board(-5, -15))
        self.assertTrue(outside_of_board(-5, SIZE + 5))
        self.assertTrue(outside_of_board(SIZE + 5, -1))
        self.assertTrue(outside_of_board(SIZE + 5, 0))
        self.assertTrue(outside_of_board(SIZE, SIZE))

    def testInsideBoard(self):
        self.assertFalse(outside_of_board(5, 4))
        self.assertFalse(outside_of_board(0, 0))

    def testValidOutsideOfBoard(self):
        board = Board(3, 2)
        # one test is sufficient since we're simply testing if outside_of_board
        # is called in valid. outside_of_board has already been tested.
        self.assertFalse(valid(-5, 2, board))

    def testValidInvalidTarget(self):
        board = Board(3, 2)
        board.rows[1][0] = 3
        self.assertFalse(valid(1, 0, board))
        self.assertTrue(valid(1, 1, board))

    def testValidTrueOnEmptyBoard(self):
        board = Board(3, 2)
        self.assertTrue(valid(1, 1, board))
    
    def testValidTrueOtherwise(self):
        board = Board(5, 5)
        board.rows[0][1] = 7
        self.assertTrue(valid(1, 4, board))

if __name__ == '__main__':
    unittest.main()
    
