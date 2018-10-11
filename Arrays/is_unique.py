#! /usr/env/python

def is_unique(in_str):
    """
    Check if the string has all unique characters.
    :param in_str:
    :return:
    """
    if len(in_str) > 128:
        return False
    char_map = {}
    for c in in_str:
        if c in char_map:
            return False
        char_map[c] = True
    return True

def is_unique2(in_str):
    """
    Check if the string has all unique characters
    :param in_str:
    :return:
    """
    if len(in_str) > 128:
        return False
    sorted_string = sorted(in_str)
    prev_char = None
    for c in sorted_string:
        if c == prev_char:
            return False
        prev_char = c
    return True

def is_unique_ascii(in_str):
    """
    Check if the string has unique characters using ascii
    :param in_str:
    :return:
    """
    if len(in_str) > 128:
        return False
    char_list = [False] * 128
    for c in in_str:
        if char_list[ord(c)]:
            return False
        char_list[ord(c)] = True
    return True

def is_unique_chars(in_str):
    """
    Check if all the unique char using bits.
    :param in_str:
    :return:
    """
    checker = 0
    if len(in_str) > 128:
        return False
    for c in in_str:
        val = ord(c)
        if checker & 1 << val > 0:
            return False
        checker |= 1 << val
    return True

def run_tests():
    assert is_unique("chandresh") == False
    assert is_unique("") == True
    assert is_unique("Palak") == False
    assert is_unique("aaaaaa") == False
    assert is_unique("abcdefgh") == True

    assert is_unique2("chandresh") == False
    assert is_unique2("") == True
    assert is_unique2("Palak") == False
    assert is_unique2("aaaaaa") == False
    assert is_unique2("abcdefgh") == True

    assert is_unique_ascii("chandresh") == False
    assert is_unique_ascii("") == True
    assert is_unique_ascii("Palak") == False
    assert is_unique_ascii("aaaaaa") == False
    assert is_unique_ascii("abcdefgh") == True

    assert is_unique_chars("chandresh") == False
    assert is_unique_chars("") == True
    assert is_unique_chars("Palak") == False
    assert is_unique_chars("aaaaaa") == False
    assert is_unique_chars("abcdefgh") == True

if __name__ == "__main__":
    run_tests()
