# test_binary.py
import unittest
from main import BinaryMultipleOfThree


class TestBinaryMultipleOfThree(unittest.TestCase):

    def setUp(self):
        self.validator = BinaryMultipleOfThree()

    def test_regex_finds_binary(self):
        text = "1100 1010 1111 abc 123"
        result = self.validator.find_binary_numbers(text)
        self.assertEqual(result, ['1100', '1010', '1111'])

    def test_multiple_of_three(self):
        self.assertTrue(self.validator.is_multiple_of_three('1100'))  # 12
        self.assertTrue(self.validator.is_multiple_of_three('1111'))  # 15
        self.assertFalse(self.validator.is_multiple_of_three('1010'))  # 10

    def test_find_multiples_in_text(self):
        text = "1100 1010 1111 1001"
        result = self.validator.find_multiples_of_three(text)
        self.assertEqual(result, ['1100', '1111', '1001'])

    def test_invalid_input(self):
        self.assertFalse(self.validator.is_multiple_of_three(''))
        self.assertFalse(self.validator.is_multiple_of_three('102'))


if __name__ == "__main__":
    unittest.main()