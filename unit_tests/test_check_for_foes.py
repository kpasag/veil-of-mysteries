import io
from unittest import TestCase
from unittest.mock import patch

from combat import check_for_foes


class Test(TestCase):
    @patch("random.randint", return_value=10)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_has_foe(self, mock_output, _):
        check_for_foes()
        expected = ("\033[93mTime freezes. A \033[95mman\033[93m appears from the darkness, "
                    "adjusts his\033[95m monocle\033[93m and smiles at you.\033[0m\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=1)
    @patch("random.choice", return_value="A\033[95m cat\033[0m stares at you, "
                                         "a faint\033[95m light glimmering in its pupil.\033[0m")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_no_foe(self, mock_output, _, __):
        check_for_foes()
        expected = ("A\033[95m cat\033[0m stares at you, "
                    "a faint\033[95m light glimmering in its pupil.\033[0m\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("random.randint", return_value=3)
    @patch("random.choice", return_value="A\033[95m woman\033[0m passes by, "
                                         "her gaze sharp behind a\033[95m monocle\033[0m.")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_no_foe_random_background(self, mock_output, _, __):
        check_for_foes()
        expected = ("A\033[95m woman\033[0m passes by, "
                    "her gaze sharp behind a\033[95m monocle\033[0m.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
