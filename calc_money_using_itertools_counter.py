from collections import Counter

"""
Note!!! Counter.update({}) method just adds its counts values(increases),
not particularly "update"s it. For example, if we want {x:1}
and we update counter with {x:10}, in the final results we won"t have
counter({x:10}), it will be counter({x:10+1}), number of count of x will be 11'
"""


def main():
    n = int(input())

    n_of_shoes = input().strip().split()

    if n != len(n_of_shoes):
        return 'Invalid input'

    counter = Counter(n_of_shoes)

    n_customers = int(input())
    money_earned = 0

    for _ in range(n_customers):
        raw_input = input().strip().split()
        _size, _price = raw_input[0], int(raw_input[1])
        _n = counter[_size]
        if _n > 0:
            money_earned += _price
            counter.update({_size: -1})

    return money_earned


if __name__ == '__main__':
    print(main())
