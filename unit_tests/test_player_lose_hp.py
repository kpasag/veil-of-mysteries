from unittest import TestCase
from unittest.mock import patch

from combat import player_lose_hp


class Test(TestCase):
    @patch("messages.type_text")
    def test_odd_hp_decreases_by_one(self, _):
        character = {"Current HP": 10, "Level": 2}
        expected = 8
        dialogue = {"player_lose_hp": (msg for msg in ["You take damage!"])}
        player_lose_hp(character, dialogue)
        actual = character["Current HP"]
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    def test_even_hp_decreases_by_one(self, _):
        character = {"Current HP": 6, "Level": 3}
        expected = 3
        dialogue = {"player_lose_hp": (msg for msg in ["You take damage!"])}
        player_lose_hp(character, dialogue)
        actual = character["Current HP"]
        self.assertEqual(expected, actual)
