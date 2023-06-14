FIRST_SEQUENCE = [3, 'Fizz']
SECOND_SEQUENCE = [5, 'Buzz']


def initialLoop(first_number=1, last_number=100):
    result = []
    for number in range(first_number, last_number+1):
        output = ''
        if isMultipleOf(number, FIRST_SEQUENCE[0]):
            output += FIRST_SEQUENCE[1]
        if isMultipleOf(number, SECOND_SEQUENCE[0]):
            output += SECOND_SEQUENCE[1]
        if output == '':
            output = str(number)
        result.append(output)
    return result


def isMultipleOf(numerator, denominator):
    return numerator % denominator == 0


if __name__ == '__main__':
    result = initialLoop(first_number=1, last_number=15)
    print('\n'.join(result))
