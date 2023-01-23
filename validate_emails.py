"""
A valid email address meets the following criteria:

1) It's composed of a username, domain name, and extension assembled in
this format: username@domain.extension

2) The username starts with an English alphabetical character, and any
subsequent characters consist of one or more of the following:
alphanumeric characters, -,., and _.

3) The domain and extension contain only English alphabetical characters.

4) The extension is 1, 2, or 3 characters in length.

Given  pairs of names and email addresses as input, print each name
and email address pair having a valid email address on a new line.

Hint: Try using Email.utils() to complete this challenge. For example,
this code:

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
"""
import re

valid_email_rgx = r'(?P<username>(^<[a-z](\w|_|\-|\.)+))@(?P<domain>([a-z]+))\.(?P<extension>([a-z]{1,3}))>'

if __name__ == '__main__':
    n = int(input())
    _inputs = []
    emails = []

    for _ in range(n):
        _inputs.append(input())

    for pair in _inputs:
        email = pair.split()[1]

        match = re.match(valid_email_rgx, email)

        if match:
            named_matches = match.groupdict()
            if len(named_matches) == 3:
                emails.append(pair)

    for email_pair in emails:
        print(email_pair)
