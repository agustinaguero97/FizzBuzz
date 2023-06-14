from unittest import TestCase
from parameterized import parameterized
from second_solution import FizzBuzz


class TestOopFizzBuzz(TestCase):

    @parameterized.expand([
        ('return_Fizz_with_num_3_deno_3', 3, 'Fizz', 3, 'Fizz'),
        ('return_Fizz_with_num_6_deno_3', 3, 'Fizz', 6, 'Fizz'),
        ('return_empty_with_num_5_deno_3', 3, 'NA', 5, ''),
        ('return_Buzz_with_num_10_deno_5', 5, 'Buzz', 10, 'Buzz'),
        ('return_Bozo_with_num_15_deno_3', 3, 'Bozo', 15, 'Bozo'),
    ])
    def test_isMultipleOfReturnWordOrEmptyString(
        self,
        _,
        denominator,
        word,
        numerator,
        expected_result
    ):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.isMultipleOfReturnWordOrEmptyString(
            numerator,
            denominator,
            word
        )
        self.assertEqual(result, expected_result)

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
        fizzbuzz = FizzBuzz(from_num, to_num)
        result = fizzbuzz.mainLoop()
        fizz_amount = result.count('Fizz')
        buzz_amount = result.count('Buzz')
        fizzbuzz_amount = result.count('FizzBuzz')
        self.assertEqual(exp_fizz, fizz_amount)
        self.assertEqual(exp_buzz, buzz_amount)
        self.assertEqual(exp_fizzbuzz, fizzbuzz_amount)

    @parameterized.expand([
        (
            'result_with_Bazz_Bozzo', ['Bazz', 2], ['Bozzo', 7],
            1, 14, True, True
        )
    ])
    def test_main_loop_with_other_sequence(
        self,
        _,
        first_sequence,
        second_sequence,
        from_num,
        to_num,
        exist_first_sequence,
        exist_second_sequence
    ):
        fizzbuzz = FizzBuzz(from_num, to_num)
        fizzbuzz.sequenceOne = first_sequence
        fizzbuzz.sequenceTwo = second_sequence
        result = fizzbuzz.mainLoop()
        self.assertEqual(first_sequence[0] in result, exist_first_sequence)
        self.assertEqual(second_sequence[0] in result, exist_second_sequence)
