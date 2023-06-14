# second solution

FIRST_SEQUENCE = ['Fizz', 3]
SECOND_SEQUENCE = ['Buzz', 5]


class FizzBuzz():
    def __init__(self, firstNumber=1, lastNumber=100) -> None:
        self.sequenceOne = FIRST_SEQUENCE
        self.sequenceTwo = SECOND_SEQUENCE
        self.firstNumber = firstNumber
        self.lastNumber = lastNumber

    def mainLoop(self) -> list:
        result = []
        for number in range(self.firstNumber, self.lastNumber + 1):
            output = ''
            output += self.isMultipleOfReturnWordOrEmptyString(
                number,
                self.sequenceOne[1],
                self.sequenceOne[0],
                )
            output += self.isMultipleOfReturnWordOrEmptyString(
                number,
                self.sequenceTwo[1],
                self.sequenceTwo[0],
                )
            if output == '':
                output = str(number)
            result.append(output)
        return result

    def isMultipleOfReturnWordOrEmptyString(
            self,
            numerator,
            sequenceNumber,
            sequenceWord
    ):
        return sequenceWord if numerator % sequenceNumber == 0 else ''


if __name__ == '__main__':
    fizzbuzz = FizzBuzz(firstNumber=1, lastNumber=1000)
    result = fizzbuzz.mainLoop()
    print('\n'.join(result))
