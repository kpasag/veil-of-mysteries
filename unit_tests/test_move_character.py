from unittest import TestCase

from player import move_character


class Test(TestCase):
    def test_move_up_w(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        move_character(character, "w")
        expected = {"X-coordinate": 2, "Y-coordinate": 1}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_down_s(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        move_character(character, "s")
        expected = {"X-coordinate": 2, "Y-coordinate": 3}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_left_a(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        move_character(character, "a")
        expected = {"X-coordinate": 1, "Y-coordinate": 2}
        actual = character
        self.assertEqual(expected, actual)

    def test_move_right_d(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        move_character(character, "d")
        expected = {"X-coordinate": 3, "Y-coordinate": 2}
        actual = character
        self.assertEqual(expected, actual)

    def test_invalid_direction(self):
        character = {"X-coordinate": 2, "Y-coordinate": 2}
        move_character(character, "x")
        expected = {"X-coordinate": 2, "Y-coordinate": 2}
        actual = character
        self.assertEqual(expected, actual)