from unittest import TestCase

from messages import colorize_text


class Test(TestCase):
    def test_single_color_token(self):
        expected = "\033[91mDanger!\033[0m"
        actual = colorize_text("{RED}Danger!{GREY}")
        self.assertEqual(expected, actual)

    def test_even_tokens(self):
        expected = "\033[96mHello\033[0m \033[92mWorld\033[0m"
        actual = colorize_text("{CYAN}Hello{GREY} {GREEN}World{GREY}")
        self.assertEqual(expected, actual)

    def test_odd_tokens(self):
        expected = "\033[96mHello\033[0m \033[92mWorld\033[0m! \033[94m:)\033[0m"
        actual = colorize_text("{CYAN}Hello{GREY} {GREEN}World{GREY}! {BLUE}:){GREY}")
        self.assertEqual(expected, actual)

    def test_no_tokens(self):
        expected = "Just text"
        actual = colorize_text("Just text")
        self.assertEqual(expected, actual)