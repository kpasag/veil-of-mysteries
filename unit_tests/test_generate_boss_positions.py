from unittest import TestCase
from unittest.mock import patch

from combat import generate_boss_positions


class Test(TestCase):
    @patch("random.choice", side_effect=[(2, 2), (4, 4), (6, 6)])
    def test_all_even_positions(self, _):
        board = {(x, y): "" for x in range(7) for y in range(7)}
        expected = ((2, 2), (4, 4), (6, 6))
        actual = generate_boss_positions(board)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=[(1, 1), (3, 3), (5, 5)])
    def test_all_odd_positions(self, _):
        board = {(x, y): "" for x in range(7) for y in range(7)}
        expected = ((1, 1), (3, 3), (5, 5))
        actual = generate_boss_positions(board)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=[(2, 3), (3, 5), (5, 2)])
    def test_all_prime_positions(self, _):
        board = {(x, y): "" for x in range(7) for y in range(7)}
        expected = ((2, 3), (3, 5), (5, 2))
        actual = generate_boss_positions(board)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=[(1, 2), (4, 3), (5, 6)])
    def test_mixed_even_odd_positions(self, _):
        board = {(x, y): "" for x in range(7) for y in range(7)}
        expected = ((1, 2), (4, 3), (5, 6))
        actual = generate_boss_positions(board)
        self.assertEqual(expected, actual)