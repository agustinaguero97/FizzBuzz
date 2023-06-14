from unittest import TestCase
from parameterized import parameterized
from src.first_solution import isMultipleOf, initialLoop


class TestFirstSolution(TestCase):

    @parameterized.expand([
        ('number_is_multiple_of', 10, 5, True),
        ('number_is_not_multiple_of', 3, 2, False)
    ])
    def test_isMultipleOf(
        self,
        _,
        numerator,
        denominator,
        expected_result
    ):
        result = isMultipleOf(numerator, denominator)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ('100_len_of_result_starts_with_0', 0, 99, 100),
        ('100_len_of_result', 1, 100, 100),
    ])
    def test_initialLoop_amount_of_strings(
        self,
        _,
        from_num,
        to_num,
        expected_lenght
    ):
        result = initialLoop(from_num, to_num)
        self.assertEqual(len(result), expected_lenght)

    @parameterized.expand([
        ('amount_of_fizz_buzz_in_range_10', 1, 10, 3, 2, 0),
        ('amount_of_fizz_buzz_in_range_15', 1, 15, 4, 2, 1),
    ])
    def test_amount_of_fizz_and_buzz_and_fizzbuzz_ocurrencess(
        self,
        _,
        from_num,
        to_num,
        exp_fizz,
        exp_buzz,
        exp_fizzbuzz,
    ):
        result = initialLoop(from_num, to_num)
        fizz_amount = result.count('Fizz')
        buzz_amount = result.count('Buzz')
        fizzbuzz_amount = result.count('FizzBuzz')
        self.assertEqual(exp_fizz, fizz_amount)
        self.assertEqual(exp_buzz, buzz_amount)
        self.assertEqual(exp_fizzbuzz, fizzbuzz_amount)
