#! /usr/env/python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        start = 0
        end = 1

        if not s:
            return 0
        max_seen = 1
        char_map[s[0]] = 0
        while end < len(s):
            cur_char = s[end]
            if cur_char in char_map:
                start = max(char_map[cur_char] + 1, start)
            char_map[cur_char] = end
            max_seen = max(end - start + 1, max_seen)
            print max_seen, start, end

            end += 1
        return max_seen
