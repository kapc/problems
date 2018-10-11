#! /usr/env/python

"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

"""
Questions:
1. upper case and lower case are same?
"""

def compress_string(in_str):
    """

    :param in_str:
    :return:
    """
    if not in_str:
        return in_str
    prev_char = None
    count = 0
    result_str = ""
    for idx in range(0, len(in_str)):
        c = in_str[idx]
        if c == prev_char:
            count += 1
        else:
            if prev_char:
                result_str += "{}{}".format(prev_char, count)
            prev_char = c
            count = 1
    result_str += "{}{}".format(c, count)
    return result_str if len(result_str) < len(in_str) else in_str

if __name__ == "__main__":
    assert "a2b1c5a3" == compress_string("aabcccccaaa")
    assert "" == compress_string("")
    assert "abcd" == compress_string("abcd")
    assert "a6" == compress_string("aaaaaa")
