from unittest import TestCase
from unittest.mock import patch

from combat import generate_bosses


class Test(TestCase):
    @patch("combat.generate_boss_positions", side_effect=[((1, 1), (2, 2), (3, 3))])
    def test_generate_bosses_structure(self, _):
        board = {(1, 1): "", (2, 2): "", (3, 3): ""}
        bosses = generate_bosses(board)
        expected = 3
        actual = len(bosses)
        self.assertEqual(expected, actual)

    @patch("combat.generate_boss_positions", side_effect=[((1, 1), (2, 2), (3, 3))])
    def test_generate_bosses_alive_true(self, _):
        board = {(1, 1): "", (2, 2): "", (3, 3): ""}
        bosses = generate_bosses(board)
        expected = True
        actual = bosses[0]["alive"]
        self.assertEqual(expected, actual)

    @patch("combat.generate_boss_positions", side_effect=[((1, 1), (2, 2), (3, 3))])
    def test_generate_bosses_level_requirement(self, _):
        board = {(1, 1): "", (2, 2): "", (3, 3): ""}
        bosses = generate_bosses(board)
        expected = 1
        actual = bosses[0]["Level_required"]
        self.assertEqual(expected, actual)