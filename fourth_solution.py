import functools
# Order changes in this list will change the end result
COMPLETE_SEQUENCE = [
    ['Fizz', 3],
    ['Buzz', 5],
]


class FizzBuzz:

    def __init__(self, fromNum=1, toNum=100) -> None:
        self.fromNum = fromNum
        self.toNum = toNum
        self.complete_seq = COMPLETE_SEQUENCE

    def loop_using_map(self):
        result = list(map(
            self.sequence_handler,
            [number for number in range(self.fromNum, self.toNum+1)]
        ))
        return result

    def sequence_handler(self, number: int):
        output = ''
        output += ''.join(list(map(
            functools.partial(return_word_or_empty, number), self.complete_seq
        )))
        if output == '':
            output = str(number)
        return output


def return_word_or_empty(number: int, sequence: list):
    wordSequence, numSequence = sequence[0], sequence[1]
    return wordSequence if number % numSequence == 0 else ''


if __name__ == '__main__':
    fizzbuzz = FizzBuzz(fromNum=1, toNum=15000)
    result = fizzbuzz.loop_using_map()
    print('\n'.join(result))
