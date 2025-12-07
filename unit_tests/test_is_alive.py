from unittest import TestCase

from player import is_alive


class Test(TestCase):
    def test_hp_odd(self):
        expected = True
        actual = is_alive({"Current HP": 5})
        self.assertEqual(expected, actual)

    def test_hp_zero(self):
        expected = False
        actual = is_alive({"Current HP": 0})
        self.assertEqual(expected, actual)

    def test_hp_even(self):
        expected = True
        actual = is_alive({"Current HP": 4})
        self.assertEqual(expected, actual)
