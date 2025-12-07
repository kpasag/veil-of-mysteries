from unittest import TestCase

from game import next_position


class Test(TestCase):
    def test_move_up_w(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        expected = (2, 1)
        actual = next_position(character, "w")
        self.assertEqual(expected, actual)

    def test_move_down_s(self):
        character = {"X-coordinate": 3, "Y-coordinate": 3}
        expected = (3, 4)
        actual = next_position(character, "s")
        self.assertEqual(expected, actual)

    def test_move_left_a(self):
        character = {"X-coordinate": 5, "Y-coordinate": 7}
        expected = (4, 7)
        actual = next_position(character, "a")
        self.assertEqual(expected, actual)

    def test_move_right_d(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        expected = (2, 1)
        actual = next_position(character, "d")
        self.assertEqual(expected, actual)

    def test_invalid_direction_returns_none(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        expected = None
        actual = next_position(character, "x")
        self.assertEqual(expected, actual)