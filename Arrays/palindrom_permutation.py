# /usr/env/python

"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

Questions:
1. Can it have a space?
2. Is the string all ascii char?
3. upper case/ lower case matter?



"""
from collections import defaultdict

def check_if_palindrom(char_dict):
    """

    :param char_dict:
    :return:
    """
    found_odd = False
    for key in char_dict:
        count = char_dict[key]
        c = key
        if count % 2 == 0:
            continue
        if found_odd and c != " ":
            return False
        found_odd = True
    return True

def permutation_palindrom(str1):
    """

    :param str1:
    :return:
    """
    str1 = str1.lower()
    char_dict = defaultdict(int)
    for i in range(0, len(str1)):
        c = str1[i]
        char_dict[c] += 1
    return check_if_palindrom(char_dict)

if __name__ == "__main__":
    assert permutation_palindrom("atco cta")
    assert permutation_palindrom("Taco cta")
    assert permutation_palindrom("ayo o ya")
    assert permutation_palindrom("")
    assert permutation_palindrom("           ")
    assert permutation_palindrom("         fsdd         sf")
