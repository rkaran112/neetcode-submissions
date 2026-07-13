"""Unit tests for the solutions under 'Data Structures & Algorithms/'.

Submission files are archived exactly as submitted to the online judge, so
they rely on a `List` name that the judge injects implicitly (see README).
To load them unmodified here, we inject `List` into the module namespace
ourselves before executing the file.
"""
import importlib.util
import os
import unittest
from typing import List

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_solution(*path_parts):
    path = os.path.join(REPO_ROOT, *path_parts)
    spec = importlib.util.spec_from_file_location("solution_under_test", path)
    module = importlib.util.module_from_spec(spec)
    module.__dict__["List"] = List
    spec.loader.exec_module(module)
    return module.Solution()


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = load_solution(
            "Data Structures & Algorithms", "is-palindrome", "submission-0.py"
        )

    def test_valid_palindrome_with_punctuation_and_case(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_empty_string_after_cleaning_is_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(" "))

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"))

    def test_even_length_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("abba"))

    def test_two_characters_not_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("0P"))


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = load_solution(
            "Data Structures & Algorithms", "buy-and-sell-crypto", "submission-1.py"
        )

    def test_typical_case(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_prices_only_decrease(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_price(self):
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_buy_on_last_day_no_profit(self):
        self.assertEqual(self.solution.maxProfit([2, 1]), 0)

    def test_constant_prices_no_profit(self):
        self.assertEqual(self.solution.maxProfit([4, 4, 4, 4]), 0)


class TestMaxProfitFirstSubmission(TestMaxProfit):
    """submission-0 is an earlier attempt at the same problem as submission-1;
    it's kept archived side by side, so it gets the same coverage."""

    def setUp(self):
        self.solution = load_solution(
            "Data Structures & Algorithms", "buy-and-sell-crypto", "submission-0.py"
        )


if __name__ == "__main__":
    unittest.main()
