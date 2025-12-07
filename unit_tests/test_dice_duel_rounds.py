from unittest import TestCase
from unittest.mock import patch

from combat import dice_duel_rounds


class Test(TestCase):
    @patch("builtins.input", return_value="")
    @patch("messages.type_text")
    @patch("combat.play_dice_round", side_effect=[1, 1])
    def test_player_wins_two_rounds(self, _, __, ___):
        expected = (2, 0)
        actual = dice_duel_rounds()
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="")
    @patch("messages.type_text")
    @patch("combat.play_dice_round", side_effect=[-1, -1])
    def test_enemy_wins_two_rounds(self, _, __, ___):
        expected = (0, 2)
        actual = dice_duel_rounds()
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="")
    @patch("messages.type_text")
    @patch("combat.play_dice_round", side_effect=[0, 1, 1])
    def test_tie_then_player_wins(self, _, __, ___):
        expected = (2, 0)
        actual = dice_duel_rounds()
        self.assertEqual(expected, actual)

    @patch("builtins.input", return_value="")
    @patch("messages.type_text")
    @patch("combat.play_dice_round", side_effect=[0, 0, 0, -1, -1])
    def test_multiple_ties_then_enemy_wins(self, _, __, ___):
        expected = (0, 2)
        actual = dice_duel_rounds()
        self.assertEqual(expected, actual)
