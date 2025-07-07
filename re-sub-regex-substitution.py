# Task
#
# You are given a text of  lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
#
# && → and
# || → or
# Both && and || should have a space " " on both sides.
#
# Input Format
#
# The first line contains the integer, .
# The next  lines each contain a line of the text.
#
# Constraints
# 0 < N < 100
#
# Neither && nor || occur in the start or end of each line.
#
# Output Format
# Output the modified text.
#
# Sample Input
#
# 11
# a = 1;
# b = input();
#
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.
# Sample Output
#
# a = 1;
# b = input();
#
# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# Note do not change &&& or ||| or & or |
# Only change those '&&' which have space on both sides.
# Only change those '|| which have space on both sides.

import re


n_lines = int(input())
for _ in range(n_lines):
    line = input()
    while ' && ' in line or ' || ' in line:
        line = re.sub(r'\s&&\s', ' and ', line)
        line = re.sub(r'\s\|\|\s', ' or ', line)

    print(line)
