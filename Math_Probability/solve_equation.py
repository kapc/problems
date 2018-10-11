#! /usr/env/python

"""

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"

"""

def parse_equation_string(in_str):
    """

    :param in_str:
    :return:
    """
    if "=" not in in_str:
        raise Exception("Invalid String")
    values = in_str.split("=")
    assert len(values) == 2, "Invalid String"

    left_x, left_total = parse_side(values[0])
    right_x, right_total = parse_side(values[1])

    if left_x - right_x == 0:
        if right_total - left_total == 0:
            return "Infinite Solutions"
        else:
            return "No solution"
    else:
        sign = 1
        if left_total - right_total == 0:
            return "0"
        if left_x - right_x < 0:
            sign = -1
        if right_total - left_total == 0:
            return "No Solutions"
        else:
            x_value = abs(left_x - right_x)
            result = (right_total - left_total) / x_value
            return result * sign

    return None

def parse_side(in_str):
    """

    :param in_str:
    :return:
    """
    total_x = 0
    total_value = 0
    idx = 0
    sign = 1
    while idx < len(in_str):
        cur_elem = in_str[idx]
        if cur_elem == "-":
            sign = -1
            idx += 1
            continue

        if cur_elem.isdigit():
            if idx + 1 < len(in_str) and in_str[idx+1] == "x":
                total_x += int(cur_elem) * sign
                idx += 1
            else:
                total_value += int(cur_elem) * sign
        elif cur_elem == "x":
            total_x += sign
        sign = 1
        idx += 1

    return int(total_x), int(total_value)


def test():
    inputs = ["x+5-3+x=6+x-2", "x=2", "x=x", "2x=x", "2x+3x-6x=x+2", "x=-1", "x=x+2"]
    for i in inputs:
        print parse_equation_string(i)

test()