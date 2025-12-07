from unittest import TestCase
from unittest.mock import patch

from messages import get_user_choice


class Test(TestCase):
    @patch("messages.type_text")
    @patch("builtins.input", return_value="N")
    def test_uppercase_letter(self, _, __):
        expected = "n"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="W")
    def test_north_uppercase_letter(self, _, __):
        expected = "w"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="A")
    def test_west_uppercase_letter(self, _, __):
        expected = "a"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="D")
    def test_east_uppercase_letter(self, _, __):
        expected = "d"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="S")
    def test_south_uppercase_letter(self, _, __):
        expected = "s"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="n")
    def test_lowercase_letter(self, _, __):
        expected = "n"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="w")
    def test_north_lowercase_letter(self, _, __):
        expected = "w"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="a")
    def test_west_lowercase_letter(self, _, __):
        expected = "a"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="d")
    def test_east_lowercase_letter(self, _, __):
        expected = "d"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="s")
    def test_south_lowercase_letter(self, _, __):
        expected = "s"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="54")
    def test_integers(self, _, __):
        expected = "54"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="3.1459265")
    def test_floats(self, _, __):
        expected = "3.1459265"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("messages.type_text")
    @patch("builtins.input", return_value="!@#$%^")
    def test_random_characters(self, _, __):
        expected = "!@#$%^"
        actual = get_user_choice()
        self.assertEqual(expected, actual)
