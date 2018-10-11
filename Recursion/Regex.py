"""

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""


class Solution(object):

    def is_match(self, s, p, s_idx, p_idx):
        if p_idx >= len(p):
            return s_idx >= len(s)

        if s_idx >= len(s):
            return p_idx + 1 < len(p) and p[p_idx + 1] == '*' and self.is_match(s, p, s_idx, p_idx + 2)

        if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
            return (self.is_match(s, p, s_idx, p_idx + 2) or
                    (s[s_idx] == p[p_idx] or p[p_idx] == '.') and self.is_match(s, p, s_idx + 1, p_idx))

        elif s[s_idx] == p[p_idx] or p[p_idx] == '.':
            return self.is_match(s, p, s_idx + 1, p_idx + 1)

        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match(s, p, 0, 0)