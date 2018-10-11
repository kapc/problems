#! /usr/env/python

"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
Hints: #300, #324, #343, #380, #394
"""

"""

As an output we need to return number of ways?
As an input you get, list of coins and total amount?

There are no floating point numbers?
"""

# Dumbest way where you can't visualize recursion.
def coins_dumb(total_amount, coin_list, count, i):
    """

    :param total_amount:
    :return:
    """
    if total_amount == 0:
        count[0] += 1
        return
    if total_amount < 0:
        return

    for i in range(i, len(coin_list)):
        coins_dumb(total_amount-coin_list[i], coin_list, count, i)

# Dumbest way 2 where you can visualize recursion and possible DP.
def coins_dumb2(total_amount, coin_list, index, memo):
    """

    :param total_amount:
    :param coin_list:
    :return:
    """
    if total_amount == 0:
        return 1

    if total_amount < 0 or index >= len(coin_list):
        return 0

    # Very important, all dynamic programming solutions require
    # memoization but here, memoization table is a tuple.
    if (total_amount, index) in memo:
        return memo[(total_amount, index)]

    count = (coins_dumb2(total_amount - coin_list[index], coin_list, index, memo) +
             coins_dumb2(total_amount, coin_list, index+1, memo))
    memo[(total_amount, index)] = count
    return count

def coins_change_1(total_amount, coin_list):
    """

    :param total_amount:
    :param coin_list:
    :return:
    """
    if total_amount == 0:
        return 1

    if not coin_list:
        return 0

    memo = [[1] + ([0] * total_amount) for _ in range(len(coin_list))]

    for i in range(len(coin_list)):
        for j in range(1, total_amount+1):
            memo[i][j] = memo[i-1][j] + (memo[i][j - coin_list[i]] if (j - coin_list[i]) >= 0 else 0)

    return memo[-1][-1]

def coins_change_2(total_amount, coin_list):
    """

    :param total_amount:
    :param coin_list:
    :return:

First note that table[i] is number of ways for coin change when N=i.

Given Algorithm fills this array (table[]) as per given set of coin (S[]). Initially all values in table[] are initialized to 0. And table[0] set to 0 (this is base case N=0).

Each coin adds up values in table[] in following manner.

For coin of value X, following are updates to table[] -

table[X] = table[X] + 1

This is easy to understand. Specifically this adds solution {X}.

for all Y > X

table[Y] = table[Y] + table[Y-X]

This is tricky to understand. Take example X = 3, and consider case for Y = 4.

4 = 3 + 1 i.e. 4 can be obtained by combining 3 and 1. And by definition number of ways to get 1 are table[1]. So that many ways are added to table[4]. Thats why above expression uses table[Y-X].

Following line in your algorithm represents the same (above two steps) -

table[j] += table[j-S[i]];
At the end of algorithm, table[n] contains solution for n.
    """
    if total_amount == 0:
        return 1

    if not coin_list:
        return 0

    memo = [1] + ([0] * total_amount)

    for i in range(len(coin_list)):
        for j in range(1, total_amount + 1):
            memo[j] += memo[j-coin_list[i]] if j - coin_list[i] >= 0 else 0

    return memo[-1]

def test_coin_change():
    """
    :return:
    """
    total_amounts = [0, -1, 10, 50, 25, 100, 250]
    results = [0, 0, 4]

if __name__ == "__main__":
    print coins_change_2(25, [1,5,10,25])
