#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s[:2]
    hour_as_int = int(hour) if hour[0] != '0' else int(hour[1])

    is_am = True if s[-2:] == 'AM' else False

    if (is_am and hour[0] == '0') or (not is_am and hour == '12'):
        return s[:-2]

    just_time = s[2:-2]

    hour_corrected = str(hour_as_int + 12) if hour_as_int + 12 != 24 else '00'

    return f'{hour_corrected}{just_time}'


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
