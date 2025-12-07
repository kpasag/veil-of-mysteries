from unittest import TestCase
from unittest.mock import patch

from combat import play_round


class Test(TestCase):
    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="test")
    def test_lower_case_correct_guess_returns_true(self, _, __):
        expected = True
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="hi")
    def test_lower_case_wrong_length_returns_false(self, _, __):
        expected = False
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="cope")
    def test_lower_case_wrong_guess_returns_false(self, _, __):
        expected = False
        actual = play_round("code")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="TEST")
    def test_upper_case_correct_guess_returns_true(self, _, __):
        expected = True
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="HI")
    def test_upper_case_wrong_length_returns_false(self, _, __):
        expected = False
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="COPE")
    def test_upper_case_wrong_guess_returns_false(self, _, __):
        expected = False
        actual = play_round("code")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="TesT")
    def test_mixed_case_correct_guess_returns_true(self, _, __):
        expected = True
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="Hi")
    def test_mixed_case_wrong_length_returns_false(self, _, __):
        expected = False
        actual = play_round("test")
        self.assertEqual(expected, actual)

    @patch("combat.input_feedback")
    @patch("builtins.input", return_value="coPe")
    def test_mixed_case_wrong_guess_returns_false(self, _, __):
        expected = False
        actual = play_round("code")
        self.assertEqual(expected, actual)