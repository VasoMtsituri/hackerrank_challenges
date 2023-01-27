"""
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z, A-Z & 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
"""
import re

upper_char_rgx = r'[A-Z]'
digits_rgx = r'\d'


def quantitative_check(_str):
    upper_chars = re.findall(upper_char_rgx, _str)

    if len(upper_chars) < 2:
        return False

    digits = re.findall(digits_rgx, _str)

    if len(digits) < 3:
        return False

    return True


def length_check(_str):
    if len(_str) != 10:
        return False

    return True


def alphanum_check(_str):
    for char in _str:
        if not char.isalnum():
            return False

    return True


def uniqueness_check(_str):
    unique_chars = set(_str)

    return len(unique_chars) == len(_str)


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        _str = input().strip()

        if length_check(_str) and uniqueness_check(_str) and\
                alphanum_check(_str) and quantitative_check(_str):
            print('Valid')
        else:
            print('Invalid')
