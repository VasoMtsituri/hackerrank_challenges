"""
Let's dive into decorators! You are given  mobile numbers. Sort them in
ascending order then print them in the standard format shown below:

The given mobile numbers may have +91, 91 or 0 written before the
actual 10-digit number. Alternatively, there may not be any prefix at all.

From this:
3
07895462130       ===>  +91 78954 62130
919875641230      ===>  +91 91959 69878
9195969878        ===>  +91 98756 41230
"""


def wrapper(f):
    def fun(l):
        standardized_numbers = []

        for number in l:
            if len(number) > 10:
                if number.startswith('0'):
                    standardized_numbers.append(
                        f'+91 {number[1:6]} {number[6:]}')
                elif number.startswith('91'):
                    standardized_numbers.append(
                        f'+{number[:2]} {number[2:7]} {number[7:]}')
                elif number.startswith('+91'):
                    standardized_numbers.append(
                        f'{number[:3]} {number[3:8]} {number[8:]}')
                else:
                    standardized_numbers.append('')
            else:
                standardized_numbers.append(f'+91 {number[:5]} {number[5:]}')
        return f(standardized_numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
