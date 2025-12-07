from unittest import TestCase
from unittest.mock import patch

from combat import play_dice_round


class Test(TestCase):
    @patch("messages.type_text")
    @patch("random.randint", side_effect=[4, 2])
    def test_player_wins_even_numbers(self, _, __):
        expected = 1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[2, 6])
    def test_boss_wins_even_numbers(self, _, __):
        expected = -1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[4, 4])
    def test_tie_even_numbers(self, _, __):
        expected = 0
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[6, 3])
    def test_player_wins_odd_numbers(self, _, __):
        expected = 1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[1, 5])
    def test_boss_wins_odd_numbers(self, _, __):
        expected = -1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[5, 5])
    def test_tie_odd_numbers(self, _, __):
        expected = 0
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[5, 2])
    def test_player_wins_mixed_numbers(self, _, __):
        expected = 1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[2, 5])
    def test_boss_wins_mixed_numbers(self, _, __):
        expected = -1
        actual = play_dice_round()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("random.randint", side_effect=[6, 6])
    def test_tie_mixed_even_numbers(self, _, __):
        expected = 0
        actual = play_dice_round()
        self.assertEqual(expected, actual)