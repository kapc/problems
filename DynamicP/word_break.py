#! /usr/env/python

"""

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


"""

def word_break_dumb(s, start, wordDict):
    """
    """
    if start >= len(s):
        return True

    word = ""
    for i in range(start, len(s)):
        word += s[i]
        if word in wordDict:
            valid = word_break_dumb(s, i + 1, wordDict)
            if valid:
                return True
    return False

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    # return self.word_break_dumb(s, 0, wordDict)
    return word_break_smart(s, wordDict)

def word_break_smart(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    lenS = len(s)

    dp = [False] * (lenS + 1)
    for i in range(0, lenS):
        for j in range(0, i + 1):
            if (j - 1 < 0 or dp[j - 1]) and s[j:i + 1] in wordDict:
                dp[i] = True
                break
    return dp[-2]

print wordBreak("leetcode", ["leet", "code"])