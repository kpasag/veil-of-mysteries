from unittest import TestCase
from unittest.mock import patch

from game import describe_current_location


class Test(TestCase):
    @patch("messages.type_text")
    def test_prints_location_coordinates(self, mock_output):
        board = {(0, 0): "Spawn Point"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        describe_current_location(board, character)
        expected = "Current Location: \033[96m(0,0)\033[0m"
        actual = mock_output.call_args_list[0][0][0]
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    def test_prints_room_description(self, mock_output):
        board = {(1, 2): "Crystal Cavern"}
        character = {"X-coordinate": 1, "Y-coordinate": 2}
        describe_current_location(board, character)
        expected = "You step into the Crystal Cavern."
        actual = mock_output.call_args_list[1][0][0]
        self.assertEqual(expected, actual)
