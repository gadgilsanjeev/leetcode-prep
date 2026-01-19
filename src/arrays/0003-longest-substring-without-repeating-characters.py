# Problem Title: Longest Substring Without Repeating Characters
# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium
# Topics: Array

"""
Explanation:
    [Briefly explain your logic here in 1-2 sentences]

Complexity:
    Time: O(n) - Explain why
    Space: O(n) - Explain why
"""

from typing import List  # Import common types as needed

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        max_cnt = 0
        cur_cnt = 0
        d = {}
        for start_ptr in xrange(len(s)-1):
            d[s[start_ptr]] = 1
            for end_ptr in xrange(start_ptr + 1, len(s)):
                cur_cnt += 1
                if s[end_ptr] in d:
                    if cur_cnt > max_cnt:
                        max_cnt = cur_cnt
                    cur_cnt = 0
                    d = {}
                    break
                else:
                    d[s[end_ptr]] = 1
            else:
                cur_cnt += 1
                if s[end_ptr] in d:
                    if cur_cnt > max_cnt:
                        max_cnt = cur_cnt
                    cur_cnt = 0
                    d = {}
                    break
                else:
                    d[s[end_ptr]] = 1
        return max_cnt