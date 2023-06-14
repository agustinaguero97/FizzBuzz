def loop_using_map(from_num=1, to_num=100):
    result = list(map(
        fizzbuzz, [number for number in range(from_num, to_num+1)]
    ))
    return result


def fizzbuzz(number):
    output = ''
    output += add_word_or_empty(number, 3, 'Fizz')
    output += add_word_or_empty(number, 5, 'Buzz')
    if output == '':
        output = str(number)
    return output


def add_word_or_empty(number, denominator, word):
    return word if number % denominator == 0 else ''


if __name__ == '__main__':
    result = loop_using_map(from_num=1, to_num=1000)
    print('\n'.join(result))
