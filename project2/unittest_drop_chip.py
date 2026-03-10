import unittest
from main import Connect4

class TestDropChip(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_successful_drop(self):
        result = self.game.drop_chip(1)

        self.assertTrue(result)
        self.assertEqual(self.game.board[5][0], 'X')

    def test_full_column(self):
        for row in range(self.game.ROWS):
            self.game.board[row][0] = 'X'

        result = self.game.drop_chip(1)

        self.assertFalse(result)

    def test_invalid_column_low(self):
        result = self.game.drop_chip(0)

        self.assertFalse(result)

    def test_invalid_column_high(self):
        result = self.game.drop_chip(8)

        self.assertFalse(result)

    def test_horizontal_win(self):
        for col in range(4):
            self.game.board[5][col] = 'X'

        self.assertTrue(self.game.check_win('X'))

    def test_vertical_win(self):
        for row in range(4):
            self.game.board[5-row][0] = 'X'

        self.assertTrue(self.game.check_win('X'))

    def test_diagonal_down_right_win(self):
        self.game.board[2][0] = 'X'
        self.game.board[3][1] = 'X'
        self.game.board[4][2] = 'X'
        self.game.board[5][3] = 'X'

        self.assertTrue(self.game.check_win('X'))

    def test_diagonal_up_right_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[4][1] = 'X'
        self.game.board[3][2] = 'X'
        self.game.board[2][3] = 'X'

        self.assertTrue(self.game.check_win('X'))

    def test_no_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.game.board[5][3] = 'O'

        self.assertFalse(self.game.check_win('X'))

if __name__ == '__main__':
    unittest.main()

"""
Test Results Documentation:

Results:
- Horizontal win detection: Passed
- Vertical win detection: Passed
- Diagonal win detection (both directions): Passed
- No win scenario: Passed

The check_win() method successfully identifies all valid winning
combinations and correctly returns False when no win exists.

No issues or bugs were detected during testing.
"""