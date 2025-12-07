from unittest import TestCase

from player import make_character


class Test(TestCase):
    def test_make_character_initial_x(self):
        character = make_character()
        expected = 0
        actual = character["X-coordinate"]
        self.assertEqual(expected, actual)

    def test_make_character_initial_y(self):
        character = make_character()
        expected = 0
        actual = character["Y-coordinate"]
        self.assertEqual(expected, actual)

    def test_make_character_initial_hp(self):
        character = make_character()
        expected = 5
        actual = character["Current HP"]
        self.assertEqual(expected, actual)

    def test_make_character_initial_level(self):
        character = make_character()
        expected = 1
        actual = character["Level"]
        self.assertEqual(expected, actual)