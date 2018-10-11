#! /usr/env/python

"""
Given two integers L and R, find the count of
numbers in the range [L, R] (inclusive) having a prime number of
set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary.
For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

"""

"""
starting range, ending range.

21 => 10101 => 3
1 => 1 => 1 False

"""

def is_prime(num):
    """

    :param num:
    :return:
    """
    i = 2
    if num == 1:
        return False
    while i ** 2 < num:
        if num % i == 0:
            return False
        i += 1

    return True

def check_bits(start, end):
    """

    :param num:
    :return:
    """
    total_count = 0
    for num in range(start, end + 1):
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num = num >> 1
        if is_prime(count):
            total_count += 1
    return total_count

print check_bits(6, 10)



