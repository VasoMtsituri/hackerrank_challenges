"""
A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

"""

import re

first_digits_rgx = r'^(4|5|6)'
non_digit_rgx = r'\D'


def check_for_first_digits(_str):
    match = re.match(first_digits_rgx, _str)

    if match:
        return True

    return False


def split_on_valid_sep(_str):
    if '-' in _str:
        parts = _str.split('-')
    else:
        parts = []

    return parts


def check_for_only_digits(_str):
    parts = split_on_valid_sep(_str)

    if parts:
        for part in parts:
            non_digits = re.findall(non_digit_rgx, part)

            if non_digits:
                return False

        return True
    else:
        non_digits = re.findall(non_digit_rgx, _str)

        if non_digits:
            return False

        return True


def check_for_length(_str):
    parts = split_on_valid_sep(_str)

    if parts:
        if len(parts) != 4:
            return False

        for part in parts:
            if len(part) != 4:
                return False
    else:
        if len(_str) != 16:
            return False

    return True


def check_for_consecutive_duplicates(_str):
    parts = split_on_valid_sep(_str)

    if parts:
        _str = ''.join(parts)

    consecutive_digit_count = 0
    consecutive_digit = ''

    for index, char in enumerate(_str):
        if index != len(_str) - 1:
            if char == _str[index + 1]:
                consecutive_digit_count += 1
                consecutive_digit = char

                if consecutive_digit_count == 4:
                    return False
            else:
                if consecutive_digit_count == 3 and char == consecutive_digit:
                    return False
                else:
                    consecutive_digit_count = 0

    return True


if __name__ == '__main__':
    n = int(input())
    results = []

    for _ in range(n):
        cc_number = input().strip()

        if check_for_first_digits(cc_number) and check_for_length(
                cc_number) and check_for_only_digits(
            cc_number) and check_for_consecutive_duplicates(cc_number):
            results.append('Valid')
        else:
            results.append('Invalid')

    for res in results:
        print(res)
