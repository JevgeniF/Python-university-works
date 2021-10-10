"""unittest tests."""

from unittest import TestCase

from quadeq import find_x


class TestFindX(TestCase):
    """Unittest Class for testing of find_x script."""

    def test_find_x_has_neg_and_pos_solution(self):
        """Checks if module finds both negative and positive solutions."""
        self.assertEqual(find_x(1, 0, -1), (-1.0, 1.0))

    def test_find_x_has_two_equal_solutions(self):
        """Checks if module finds equal solution, x1 == x2."""
        self.assertEqual(find_x(1, 0, 0), 0.0)

    def test_find_x_has_no_solutions(self):
        """Checks if module informs that there are no solutions."""
        self.assertEqual(find_x(1, 0, 1), "No solutions")

    def test_find_x_is_linear_with_one_solution(self):
        """Checks if module finds solution for linear equation, a == 0."""
        self.assertEqual(find_x(0, 0.5, 1), -2.0)
