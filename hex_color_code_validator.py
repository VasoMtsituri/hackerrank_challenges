"""
Input:
11

#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}

The right output:
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

"""

import re

hex_color_rgx = r'(#[0-9a-f]{3,6})(;|,|\))'


def detect_hex_color_codes(_str):
    codes = re.findall(hex_color_rgx, _str, re.IGNORECASE)

    if codes:
        return [x[0] for x in codes]

    return []


if __name__ == '__main__':
    n = int(input().strip())
    all_hex_codes = []

    for _ in range(n):
        codes = detect_hex_color_codes(_str=input().strip())
        all_hex_codes.extend(codes)

    for _code in all_hex_codes:
        print(_code)
