from unittest import TestCase

from game import check_if_goal_attained


class Test(TestCase):
    def test_amon_dead_returns_true(self):
        bosses = ({"name": "Amon, the God of Mischief", "alive": False, "level": 1},
                  {"name": "Enzo", "alive": True, "level": 2},
                  {"name": "Hvin", "alive": True, "level": 3})
        expected = True
        actual = check_if_goal_attained(bosses)
        self.assertEqual(expected, actual)

    def test_amon_alive_returns_false(self):
        bosses = ({"name": "Amon, the God of Mischief", "alive": True, "level": 1},
                  {"name": "Enzo", "alive": False, "level": 2},
                  {"name": "Hvin", "alive": False, "level": 3})
        expected = False
        actual = check_if_goal_attained(bosses)
        self.assertEqual(expected, actual)

    def test_no_amon_present_returns_true(self):
        bosses = ({"name": "Not Amon", "alive": True, "level": 10},
                  {"name": "Something Else", "alive": False, "level": 20})
        expected = True
        actual = check_if_goal_attained(bosses)
        self.assertEqual(expected, actual)