import io
from unittest import TestCase
from unittest.mock import patch

from messages import validate_move_message


class Test(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_move_north_message(self, mock_output):
        board = {(0, 0): "A", (0, 1): "B",
                 (1, 0): "C", (1, 1): "D"}
        character = {"X-coordinate": 1, "Y-coordinate": 0}
        validate_move_message(character, board, "w")
        expected = "You can't go further north.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_move_south_message(self, mock_output):
        board = {(0, 0): "A", (0, 1): "B",
                 (1, 0): "C", (1, 1): "D"}
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        validate_move_message(character, board, "s")
        expected = "You can't go further south.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_move_west_message(self, mock_output):
        board = {(0, 0): "A", (0, 1): "B",
                 (1, 0): "C", (1, 1): "D"}
        character = {"X-coordinate": 0, "Y-coordinate": 1}
        validate_move_message(character, board, "a")
        expected = "You can't go further west.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_move_east_message(self, mock_output):
        board = {(0, 0): "A", (0, 1): "B",
                 (1, 0): "C", (1, 1): "D"}
        character = {"X-coordinate": 1, "Y-coordinate": 0}
        validate_move_message(character, board, "d")
        expected = "You can't go further east.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_direction_message(self, mock_output):
        board = {(0, 0): "A", (0, 1): "B",
                 (1, 0): "C", (1, 1): "D"}
        character = {"X-coordinate": 0, "Y-coordinate": 0}
        validate_move_message(character, board, "x")
        expected = "Please try again.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)