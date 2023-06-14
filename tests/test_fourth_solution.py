from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from fourth_solution import (
    FizzBuzz,
    return_word_or_empty
)
from scenarios import (
    FIZZ,
    BAZZ,
    FIZZBUZZ,
    RESULT_FIZZBAZZBUZZ_FROM_1_TO_15,
    FIZZBAZZBUZZ
)


def fizzbuzz_init(from_num, to_num, comp_seq=FIZZBUZZ):
    fizzbuzz = FizzBuzz(from_num, to_num)
    fizzbuzz.complete_seq = comp_seq
    return fizzbuzz


class TestFourthSolution(TestCase):

    @parameterized.expand([
        (
            'enter_bazz_and_seq_return_bazz',
            BAZZ, 14, 'Bazz'),
        (
            'enter_fizz_seq_return_empty',
            FIZZ, 1, ''),
    ])
    def test_return_word_or_empty(
        self,
        _,
        sequence,
        numerator,
        expected_result,
    ):
        result = return_word_or_empty(numerator, sequence)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ('num_15_should_return_FizzBuzz', 15, FIZZBUZZ, 'FizzBuzz'),
        ('num_1_should_return_str_1', 1, FIZZBUZZ, '1'),
        (
            'num_105_should_return_FizzBazzBuzz',
            105, FIZZBAZZBUZZ, 'FizzBazzBuzz'
        ),
    ])
    def test_fizzbuzz(self, _, number, complete_seq, expected_output):
        patch('fourth_solution.COMPLETE_SEQUENCE', complete_seq)
        fizzbuzz = FizzBuzz()
        fizzbuzz.complete_seq = complete_seq
        result = fizzbuzz.sequence_handler(number)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        (
            'correct_fizzbazzbuzz_for_range_1_to_15',
            1, 15, FIZZBAZZBUZZ, RESULT_FIZZBAZZBUZZ_FROM_1_TO_15
        ),
    ])
    def test_loop_using_map(
        self,
        _,
        from_num,
        to_num,
        complete_seq,
        expected_output
    ):
        fizzbuzz = fizzbuzz_init(from_num, to_num, complete_seq)
        result = fizzbuzz.loop_using_map()
        self.assertEqual(result, expected_output)
