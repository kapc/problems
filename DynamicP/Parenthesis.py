#! /usr/env/python

"""
Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output:
((())), (()()), ()()(), ()(())
"""

def print_all_pairs(opened, closed, till_now, n, solution):
    """

    :param opened:
    :param closed:
    :return:
    """
    if opened < 0 or closed < opened:
        return
    if closed == 0 :
        solution.append(till_now)
        return

    print_all_pairs(opened-1, closed, till_now + '(', n, solution)
    print_all_pairs(opened, closed-1, till_now  + ')', n, solution)

def print_all(n):
    """

    :param n:
    :return:
    """
    solution = []
    if n == 0:
        return 0
    print_all_pairs(n, n, "", n, solution)
    print solution
    return len(solution)


def test_print_all_pairs():
    test_inputs = [3, 1, 2, 0, 10]
    results = [5, 1, 2, 0, 16796]

    print_all(3)
    for input_t, result_t in zip(test_inputs, results):
        assert result_t == print_all(input_t), print_all(input_t)

print_all(3)
