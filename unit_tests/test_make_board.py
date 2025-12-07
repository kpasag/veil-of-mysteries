from unittest import TestCase
from unittest.mock import patch

from game_board import make_board


class Test(TestCase):
    @patch("random.choice", return_value="Cell")
    def test_make_board_one_by_one(self, _):
        expected = {(0, 0): "Cell"}
        actual = make_board(1, 1)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["Room A", "Room B", "Room C", "Room D"])
    def test_make_board_two_by_two(self, _):
        expected = {(0, 0): "Room A",
                    (0, 1): "Room B",
                    (1, 0): "Room C",
                    (1, 1): "Room D"}
        actual = make_board(2, 2)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["X", "Y", "Z"])
    def test_make_board_three_by_one(self, _):
        expected = {(0, 0): "X",
                    (1, 0): "Y",
                    (2, 0): "Z"}
        actual = make_board(3, 1)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["Alpha", "Beta", "Gamma"])
    def test_make_board_one_by_three(self, _):
        expected = {(0, 0): "Alpha",
                    (0, 1): "Beta",
                    (0, 2): "Gamma"}
        actual = make_board(1, 3)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"])
    def test_make_board_two_by_three(self, _):
        expected = {(0, 0): "Alpha", (0, 1): "Beta", (0, 2): "Gamma",
                    (1, 0): "Delta", (1, 1): "Epsilon", (1, 2): "Zeta"}
        actual = make_board(2, 3)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["Dog", "Cat", "Fox", "Wolf", "Bear",
                                         "Hawk", "Eagle", "Shark", "Tiger"])
    def test_make_board_three_by_three(self, _):
        expected = {(0, 0): "Dog", (0, 1): "Cat", (0, 2): "Fox",
                    (1, 0): "Wolf", (1, 1): "Bear", (1, 2): "Hawk",
                    (2, 0): "Eagle", (2, 1): "Shark", (2, 2): "Tiger"}
        actual = make_board(3, 3)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=[f"A{i}" for i in range(1, 17)])
    def test_make_board_four_by_four(self, _):
        expected = {(0, 0): "A1", (0, 1): "A2", (0, 2): "A3", (0, 3): "A4",
                    (1, 0): "A5", (1, 1): "A6", (1, 2): "A7", (1, 3): "A8",
                    (2, 0): "A9", (2, 1): "A10", (2, 2): "A11", (2, 3): "A12",
                    (3, 0): "A13", (3, 1): "A14", (3, 2): "A15", (3, 3): "A16"}
        actual = make_board(4, 4)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["AK-47 | Redline", "M4A1-S | Printstream", "AWP | Asiimov",
                                         "Desert Eagle | Blaze", "USP-S | Kill Confirmed",
                                         "AK-47 | Vulcan", "M4A4 | Howl", "AWP | Dragon Lore", "Glock-18 | Fade",
                                         "P250 | See Ya Later", "AK-47 | Case Hardened", "M4A1-S | Hot Rod",
                                         "Scout | Blood in the Water", "P90 | Death by Kitty", "FAMAS | Commemoration",
                                         "AK-47 | Neon Rider", "M4A4 | Poseidon", "AWP | Hyper Beast",
                                         "CZ75 | Victoria", "Tec-9 | Fuel Injector", "AK-47 | The Empress",
                                         "M4A1-S | Chantico's Fire", "Five-SeveN | Monkey Business",
                                         "MAC-10 | Neon Rider", "P2000 | Fire Elemental"])
    def test_make_board_five_by_five(self, _):
        expected = {
            (0, 0): "AK-47 | Redline",
            (0, 1): "M4A1-S | Printstream",
            (0, 2): "AWP | Asiimov",
            (0, 3): "Desert Eagle | Blaze",
            (0, 4): "USP-S | Kill Confirmed",
            (1, 0): "AK-47 | Vulcan",
            (1, 1): "M4A4 | Howl",
            (1, 2): "AWP | Dragon Lore",
            (1, 3): "Glock-18 | Fade",
            (1, 4): "P250 | See Ya Later",
            (2, 0): "AK-47 | Case Hardened",
            (2, 1): "M4A1-S | Hot Rod",
            (2, 2): "Scout | Blood in the Water",
            (2, 3): "P90 | Death by Kitty",
            (2, 4): "FAMAS | Commemoration",
            (3, 0): "AK-47 | Neon Rider",
            (3, 1): "M4A4 | Poseidon",
            (3, 2): "AWP | Hyper Beast",
            (3, 3): "CZ75 | Victoria",
            (3, 4): "Tec-9 | Fuel Injector",
            (4, 0): "AK-47 | The Empress",
            (4, 1): "M4A1-S | Chantico's Fire",
            (4, 2): "Five-SeveN | Monkey Business",
            (4, 3): "MAC-10 | Neon Rider",
            (4, 4): "P2000 | Fire Elemental"
        }
        actual = make_board(5, 5)
        self.assertEqual(expected, actual)