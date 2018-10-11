# /usr/env/python

"""
1.9 String Rotation: Assume you have a method i5Substring which checks ifone word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., Uwaterbottleuis a rotation ofuerbottlewatU ).

"""
def check_if_string_rotation(s1, s2):
    """

    :param s1:
    :param s2:
    :return:
    """
    result_string = s1 + s1
    if s2 in result_string:
        return True
    return False


if __name__ == "__main__":
    s1 = "erbottlewat"
    s2 = "waterbottle"
    print(check_if_string_rotation(s1, s2))