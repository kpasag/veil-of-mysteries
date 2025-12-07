from unittest import TestCase
from unittest.mock import patch

from game import validate_move


class Test(TestCase):
    @patch("messages.validate_move_message")
    def test_move_up_valid_returns_true(self, _):
        board = {(0, 0): "Room", (0, 1): "Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 1}
        expected = True
        actual = validate_move(board, character, "w")
        self.assertEqual(expected, actual)

    @patch("messages.validate_move_message")
    def test_move_down_valid_returns_true(self, _):
        board = {(0, 0): "Room", (0, 1): "Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = True
        actual = validate_move(board, character, "s")
        self.assertEqual(expected, actual)

    @patch("messages.validate_move_message")
    def test_move_left_valid_returns_true(self, _):
        board = {(0, 0): "Room", (1, 0): "Room"}
        character = {"X-coordinate": 1, "Y-coordinate": 0}
        expected = True
        actual = validate_move(board, character, "a")
        self.assertEqual(expected, actual)

    @patch("messages.validate_move_message")
    def test_move_right_valid_returns_true(self, _):
        board = {(0, 0): "Room", (1, 0): "Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = True
        actual = validate_move(board, character, "d")
        self.assertEqual(expected, actual)

    @patch("messages.validate_move_message")
    def test_move_outside_board_returns_false(self, _):
        board = {(0, 0): "Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = validate_move(board, character, "w")
        self.assertEqual(expected, actual)

    @patch("messages.validate_move_message")
    def test_invalid_direction_returns_false(self, _):
        board = {(0, 0): "Room"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = validate_move(board, character, "x")
        self.assertEqual(expected, actual)

